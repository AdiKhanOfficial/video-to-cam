
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
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Place a video file named `video.mp4` in the project directory, or modify the script to point to another video.

## Usage
Run the application:
```bash
python main.py
```

### Controls
- **Pause/Play**: Press `p`
- **Zoom In**: Press `z`
- **Zoom Out**: Press `x`
- **Move Up**: Press `u`
- **Move Down**: Press `d`
- **Move Left**: Press `l`
- **Move Right**: Press `r`
- **Exit**: Press `esc`

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## License
This project is licensed under the [MIT License](LICENSE).
