import os
import cv2
import streamlit as st
import glob
from PIL import Image

# Define the model path
model_path = 'yolov8sbest.pt'

# Detect number of cameras
cams = 0
for i in range(10):
    cam = cv2.VideoCapture(i, cv2.CAP_DSHOW)
    if cam.isOpened():
@@ -24,19 +28,45 @@
except:
    pass

for i in range(cams):
    try:
        cam_dir = f"{cap_dir}\\CAMERA{i+1}"
        os.mkdir(cam_dir)
    except:
        pass

# Front end
st.title("Security Surveillance")
st.sidebar.text(f"Available cameras: {cams}")
st.sidebar.write("---")
st.sidebar.info("Click to view camera feeds.")

# Handle page navigation manually
page = st.sidebar.radio("Select Camera Feed", ["Home"] + [f"Camera Feed {i+1}" for i in range(cams)])

@@ -50,24 +80,3 @@
    # For example, use the camera feed capturing logic to show images
    # For simplicity, let's assume you load the camera feed and display images
    st.write(f"Displaying feed from Camera {camera_id + 1}")
# New Feature: Security Logs
if st.sidebar.button("Security Logs"):
    # Let the user select which camera's logs to view
    camera_choice = st.radio("Select Camera", [f"Camera {i+1}" for i in range(cams)])
    # Get the folder for the selected camera
    camera_folder = f"{cap_dir}\\{camera_choice.replace(' ', '')}"
    # Get all image files in the selected camera's folder
    image_files = glob.glob(os.path.join(camera_folder, "*.png"))
    image_files.sort()  # Sort images by filename or timestamp
    # Show images in a grid format
    if image_files:
        cols = st.columns(3)  # Display images in 3 columns (adjust as needed)
        for i, image_file in enumerate(image_files):
            img = Image.open(image_file)
            col = cols[i % 3]
            col.image(img, use_column_width=True, caption=f"Image {i+1}")
    else:
        st.write("No images found in this camera's directory.")
