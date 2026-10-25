# Nagar Drishti AI for Windows OS

1. **Clone the repository**
  ```powershell
  git clone https://github.com/yash-2008-yash/nagar-drishti-ai.git
  ```

2. **Create a virtual environment**
  ```powershell
  cd nagar-drishti-ai
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  ```

3. **Install dependencies**
  ```powershell
  pip install ultralytics streamlit opencv-python pillow
  ```
  > **NOTE:** The dependencies are huge in size, so downloading might take a while.

4. **Start the app**
  ```powershell
  streamlit run app.py
  ```