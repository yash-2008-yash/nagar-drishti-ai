import streamlit as st
from ultralytics import YOLO
import cv2
from PIL import Image
import tempfile
import os
from pathlib import Path

# ---------- Configuration ----------

st.set_page_config(page_title="Nagar Drishti AI", page_icon="🧿", layout="wide")

CONFIDENCE_THRESHOLD = 0.15     # Minimum confidence for a detection to be kept
FRAME_STEP = 5                  # Analyse every Nth frame of the video
RESIZE_DIMENSIONS = (640, 360)  # (width, height) used for video inference


# ---------- Styling ----------

def load_css(file_name):
    css_path = Path(__file__).parent / file_name
    st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)

load_css("style.css")


# ---------- Model loading ----------

@st.cache_resource  # keeps the model in memory, avoiding a reload every time
def load_model():
    return YOLO("pothole.pt")

model = load_model()


# ---------- Page Header ----------

st.markdown(
    """
    <div class = "hero">
        <h1>NAGAR DRISHTI AI</h1>
        <div class = "tagline">AI-POWERED MOBILE URBAN INTELLIGENCE PLATFORM USING PUBLIC TRANSPORT FLEET</div>
        <div class = "team">
            Prototype by
            <span class = "poppins">Yashwanth M</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)


# ---------- File upload ----------

uploaded = st.file_uploader(
    "Upload an image or video and get annotated detections of the potholes.",
    type=["jpg", "jpeg", "png", "mp4", "avi", "mov", "mkv"],
)

if uploaded:
    is_video = uploaded.type.startswith("video")

    # ---------- Image Workflow ----------
    
    if not is_video:
        image = Image.open(uploaded).convert("RGB")
        st.image(image, caption="Input road image", width="stretch")

        if st.button("Detect Potholes", type="primary"):
            with st.spinner("AI analysing road..."):
                result = model.predict(image, conf=CONFIDENCE_THRESHOLD, verbose=False)[0]

            count = len(result.boxes)
            left, right = st.columns(2)
            left.metric("Potholes detected", count)
            right.metric(
                "Highest confidence",
                # default=0 prevents an error when no potholes are detected.
                f"{max((float(b.conf[0]) for b in result.boxes), default=0):.1%}",
            )

            st.image(
                result.plot()[:, :, ::-1],
                caption="AI detection results",
                width="stretch",
            )

    # ---------- Video Workflow ----------
    else:
        st.video(uploaded)

        if st.button("Analyse Video", type="primary"):
            input_path = output_path = None
            cap = writer = None

            try:
                with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as f:
                    f.write(uploaded.getvalue())
                    input_path = f.name

                cap = cv2.VideoCapture(input_path)
                fps = cap.get(cv2.CAP_PROP_FPS) or 25
                total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                if total <= 0 or not cap.isOpened():
                    st.error("Could not read this video. Try another MP4.")
                    st.stop()

                step = FRAME_STEP
                output_fps = max(1, fps / step)

                progress = st.progress(0)
                status = st.empty()

                output = tempfile.NamedTemporaryFile(suffix=".mp4", delete=False)
                output_path = output.name
                output.close()

                writer = None
                detections = 0
                frames_done = 0
                frame_no = 0
                last_frame = None

                # Main loop: read frames sequentially until the video ends.
                while True:
                    ok, frame = cap.read()
                    if not ok:
                        break

                    # Run inference only on the sampled frames.
                    if frame_no % step == 0:
                        frame = cv2.resize(frame, RESIZE_DIMENSIONS)
                        result = model.predict(frame, conf=CONFIDENCE_THRESHOLD, verbose=False)[0]
                        detections += len(result.boxes)
                        last_frame = result.plot()
                        frames_done += 1

                        if writer is None:
                            h, w = last_frame.shape[:2]
                            writer = cv2.VideoWriter(
                                output_path,
                                cv2.VideoWriter_fourcc(*"mp4v"),
                                output_fps,
                                (w, h),
                            )

                        if not writer.isOpened():
                            st.error("Could not create output video.")
                            st.stop()

                        writer.write(last_frame)

                        progress.progress(min(1.0, frame_no / total))
                        status.write(f"Analysing frame {frame_no + 1} / {total}")

                    frame_no += 1

                cap.release()
                cap = None
                writer.release()
                writer = None

                st.success(
                    f"Analysis complete! {detections} detections across {frames_done} sampled frames."
                )
                st.caption(
                    "Video sampled at every 5th frame. Detection count may include the same pothole in multiple frames."
                )

                with open(output_path, "rb") as f:
                    st.download_button(
                        "Download analysed video",
                        f,
                        file_name="nagar-drishti-annotated-footage.mp4",
                        mime="video/mp4",
                    )

            except Exception as e:
                st.error(f"Video processing failed: {e}")
            finally:
                if cap is not None:
                    cap.release()
                if writer is not None:
                    writer.release()
                for path in (input_path, output_path):
                    if path and os.path.exists(path):
                        try:
                            os.unlink(path)
                        except OSError:
                            pass