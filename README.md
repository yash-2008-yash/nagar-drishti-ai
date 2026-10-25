<p align="center">
  <picture>
    <img alt="Nagar Drishti AI" src="./assets/logo.png" width="350" style="max-width: 100%;">
  </picture>
</p>

<h3 align="center">Turning everyday buses into moving road-health sensors.</h3>

<p align="center">
  Upload a road image or video, and get every pothole detected, marked, and counted in seconds.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/SMART%20INDIA%20HACKATHON-2026-006400?style=for-the-badge&labelColor=000000" alt="Smart India Hackathon 2026">
</p>

<p align="center">
  <a href="#tech-stack">Tech Stack</a> •
  <a href="#features">Features</a> •
  <a href="#installation">Installation</a> •
  <a href="#contribution">Contribution</a>
</p>

---

## The Problem

Potholes damage vehicles, cause accidents, and quietly get worse with every monsoon. Cities usually find out about them late, through complaints or slow manual surveys, because nobody can afford to inspect every road, every day.

Over 9,438 lives were lost in India to pothole accidents between 2020 and 2024.
[(SOURCE)](https://thelogicalindian.com/over-9438-lives-lost-in-india-to-pothole-accidents-between-2020-and-2024-uttar-pradesh-reports-5127-deaths/)

## The Fix

**Nagar Drishti AI** is an *AI-powered mobile urban intelligence platform using the public transport fleet*. The idea is simple: buses already cover a city's roads every day, so a camera on them can watch the road surface for free.

This repository is the **working prototype of the detection module**. It runs a custom-trained YOLO model on road images and videos and returns the annotated result, so the detection pipeline can be demonstrated end to end.

## Tech Stack

- **Python** — The core language
- **Streamlit** — Web interface, file uploads, progress feedback, and downloads
- **Ultralytics YOLO** — Custom-trained pothole detection model
- **OpenCV** — Reading video frames, resizing, and writing the annotated output video
- **Pillow** — Image loading and conversion
- **CSS** — Styling the web interface

## Features

- 🖼️ Pothole detection on images (JPG, JPEG, PNG)
- 🎥 Pothole detection on videos (MP4, AVI, MOV, MKV)
- 📊 Live metrics: number of potholes detected and highest confidence score
- 🟩 Annotated output with bounding boxes drawn on every detection
- ⏳ Real-time progress bar while a video is being analysed
- ⬇️ One-click download of the annotated video
- 🧠 Model cached in memory, so it loads only once per session
- 🧹 Temporary files cleaned up automatically after processing

## Installation

**Prerequisites:** Python 3.10 or newer, and the trained model file `pothole.pt` placed in the project root.

- [Nagar Drishti AI for Windows](./installation/windows.md)
- [Nagar Drishti AI for Linux](./installation/linux.md)
- [Nagar Drishti AI for macOS](./installation/mac.md)

## Contribution

This is an open-source project. Feel free to contribute.

1. Fork the repo
2. Create a branch — `git checkout -b feature/your-feature`
3. Make your changes
4. Commit — `git commit -m "Add: your feature"`
5. Push — `git push origin feature/your-feature`
6. Open a Pull Request

For major changes, open an issue first so we can talk it through.

---

<p align="center">
  Built by <a href="https://github.com/yash-2008-yash">Yashwanth M</a> for Smart India Hackathon 2026.
</p>