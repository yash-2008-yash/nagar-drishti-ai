# Nagar Drishti AI for Linux (Ubuntu / Debian)

1. **Clone the project**
  ```bash
  git clone https://github.com/yash-2008-yash/nagar-drishti-ai.git
  ```

2. **Create a virtual environment**
  ```bash
  cd nagar-drishti-ai
  python3 -m venv .venv
  source .venv/bin/activate
```

3. **Install dependencies**
  ```bash
  pip install ultralytics streamlit opencv-python pillow
  ```
  > **NOTE:** The dependencies are huge in size, so downloading might take a while.

4. **Start the app**
  ```bash
  streamlit run app.py
  ```