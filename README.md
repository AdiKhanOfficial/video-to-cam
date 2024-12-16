# Video to Cam

A Python application that streams a video file through a virtual camera with real-time zoom, pan, and playback control.

## Features
- Stream video to a virtual camera in real-time.
- **Zoom**: Adjust video zoom using `z` (zoom in) and `x` (zoom out).
- **Pan**: Move the video viewport using `u` (up), `d` (down), `l` (left), and `r` (right).
- **Pause/Play**: Toggle playback using `p`.
- **Exit**: Quit the app with `esc`.

## Requirements
- Python 3.x
- Dependencies:
  - OpenCV
  - pyvirtualcam
  - numpy
  - keyboard

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/video-to-cam.git
   cd video-to-cam
