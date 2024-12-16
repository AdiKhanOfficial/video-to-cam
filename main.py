import cv2
import pyvirtualcam
import numpy as np
import keyboard
import time
import sys
import os

# Determine the path to the executable or script
print(os.path.dirname(sys.executable))
if hasattr(sys, '_MEIPASS'):
    base_path = os.path.dirname(sys.executable)
else:
    base_path = os.path.dirname(__file__)

video_path = os.path.join(base_path, "video.mp4")
paused = False
zoom_factor = 1.0
offset_x, offset_y = 0, 0  # Initial offset values
zoom_step = 0.05
last_key_time = 0

# Initialize video capture
cap = cv2.VideoCapture(video_path)
if not cap.isOpened():
    print(f"Error: Cannot open video file '{video_path}'.")
    sys.exit()

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

try:
    with pyvirtualcam.Camera(width=width, height=height, fps=fps, fmt=pyvirtualcam.PixelFormat.BGR) as cam:
        print("Virtual Camera Started. Press ESC to exit.")
        start_time = time.time()

        while True:
            current_time = time.time()

            # Handle play/pause
            if keyboard.is_pressed('p'):
                if current_time - last_key_time > 0.3:  # 300ms debounce
                    paused = not paused
                    last_key_time = current_time

            # Handle zoom
            if keyboard.is_pressed('z') and zoom_factor < 3.0:
                zoom_factor += zoom_step
            if keyboard.is_pressed('x') and zoom_factor > 1.0:
                zoom_factor -= zoom_step

            # Reset position when zooming out to the initial zoom factor (1.0)
            if zoom_factor == 1.0:
                offset_x = 0
                offset_y = 0

            # Handle movement
            if keyboard.is_pressed('u'):  # Move up
                offset_y = max(offset_y - 10, -height // 2)
            if keyboard.is_pressed('d'):  # Move down
                offset_y = min(offset_y + 10, height // 2)
            if keyboard.is_pressed('r'):  # Move right
                offset_x = max(offset_x - 10, -width // 2)
            if keyboard.is_pressed('l'):  # Move left
                offset_x = min(offset_x + 10, width // 2)

            # Exit on ESC
            if keyboard.is_pressed('esc'):
                break

            # Read the next frame if not paused
            if not paused:
                ret, frame = cap.read()
                if not ret:  # Loop video
                    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    ret, frame = cap.read()

            if frame is not None:
                h, w, _ = frame.shape
                center_x, center_y = w // 2, h // 2
                cropped_w, cropped_h = int(w / zoom_factor), int(h / zoom_factor)
                cropped_x1 = max(center_x - cropped_w // 2 + offset_x, 0)
                cropped_y1 = max(center_y - cropped_h // 2 + offset_y, 0)
                cropped_x2 = min(cropped_x1 + cropped_w, w)
                cropped_y2 = min(cropped_y1 + cropped_h, h)

                cropped_frame = frame[cropped_y1:cropped_y2, cropped_x1:cropped_x2]
                processed_frame = cv2.resize(cropped_frame, (w, h), interpolation=cv2.INTER_LINEAR)

                # Send to virtual camera
                cam.send(processed_frame)
                cam.sleep_until_next_frame()

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    cap.release()
    print("Virtual Camera Closed.")
