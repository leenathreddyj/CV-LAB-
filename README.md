# CV Lab

### Computer Vision Web Application

**Author:** Sai Leenath Jampala

---

A comprehensive web-based platform for real-time computer vision processing, featuring advanced image analysis, object tracking, pose estimation, and more.

## Overview

CV Lab provides seven specialized modules for computer vision tasks:

| Module | Description |
|--------|-------------|
| **01** | Dimension Estimation — Measure real-world dimensions using perspective projection |
| **02** | Template Matching — Find objects in images with Fourier restoration |
| **03** | Feature Detection — Gradients, edges, corners, and segmentation analysis |
| **04** | Image Stitching — Create panoramas with SIFT and homography |
| **05-06** | Object Tracking — Real-time marker-based and marker-less tracking |
| **07** | Pose & Hand — AI-powered body pose and hand gesture recognition |

---

## Getting Started

### Requirements

- Python 3.11+
- pip

### Installation

```bash
# Clone the repository
git clone <repository-url>
cd Computer-Vision-Application

# Create virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

### Access

Open your browser and navigate to:

```
http://localhost:5000
```

Use the **Developer Login** for quick access without registration.

---

## Modules

### Module 01: Dimension Estimation

Measure real-world object dimensions from images using camera calibration and perspective projection.

- Upload an image (lens distortion auto-corrected)
- Click up to 4 points to measure distances
- Formula: `W_real = (W_pixel × D) / f`

### Module 02: Template Matching

Locate template images within larger scenes using normalized cross-correlation.

- Multi-template support
- Adjustable confidence threshold
- Fourier-based image restoration

### Module 03: Feature Detection

Comprehensive feature analysis toolkit:

- Gradient magnitude and angle visualization
- Laplacian of Gaussian (LoG) edge detection
- Custom edge detection with NMS + hysteresis
- Harris corner detection
- Boundary detection
- ArUco marker segmentation

### Module 04: Image Stitching

Create panoramas from multiple overlapping images.

- SIFT feature detection (OpenCV and custom implementation)
- FLANN-based feature matching
- RANSAC homography estimation

### Module 05-06: Object Tracking

Real-time object tracking with multiple methods:

- **Marker-based:** ArUco markers, QR codes
- **Marker-less:** Template matching, optical flow
- **SAM2:** Segmentation mask overlay from NPZ files

### Module 07: Pose & Hand Tracking

AI-powered human tracking using MediaPipe:

- Full body pose estimation (33 landmarks)
- Hand tracking (21 landmarks per hand)
- Gesture recognition
- Body position detection (standing, sitting, etc.)
- CSV data export

---

## Tech Stack

| Layer | Technologies |
|-------|-------------|
| Backend | Flask, OpenCV, NumPy, SciPy, MediaPipe |
| Frontend | HTML5, CSS3, JavaScript, Canvas API |
| Database | SQLite |
| Deployment | Docker, Gunicorn |

---

## Project Structure

```
├── app.py                 # Application entry point
├── api_routes.py          # API endpoints
├── config.py              # Configuration
├── modules/               # CV processing modules
│   ├── module1_dimension.py
│   ├── module2_template.py
│   ├── module3_features.py
│   ├── module4_sift_stitching.py
│   ├── module5_tracking.py
│   └── module7_pose_hand.py
├── templates/             # HTML templates
├── static/                # CSS and JavaScript
│   ├── css/
│   └── js/
└── requirements.txt       # Dependencies
```

---

## Configuration

Set environment variables for production:

```bash
FLASK_ENV=production
PORT=5000
SECRET_KEY=<your-secret-key>
```

---

## License

Educational project © 2025 Sai Leenath Jampala

---

Built with Flask & OpenCV
