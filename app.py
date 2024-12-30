import os
import cv2
import streamlit as st
from ultralytics import YOLO
import supervision as sv

# Install necessary dependencies for cloud environments (streamlit cloud or otherwise)
import os
os.system('pip install opencv-python-headless==4.8.0.74')

# Initialize variables
model_path = 'yolov8sbest.pt'
cams = 0

# Detect number of cameras
for i in range(10):
    cam = cv2.VideoCapture(i, cv2.CAP_DSHOW)
    if cam.isOpened():
        cams += 1
        cam.release()
    else:
        break

root_dir = os.getcwd()
cap_dir = f"{root_dir}\\CAPTURES"
try:
    os.mkdir(cap_dir)
except:
    pass

# Create directories for each camera
for i in range(cams):
    try:
        cam_dir = f"{cap_dir}\\CAMERA{i+1}"
        os.mkdir(cam_dir)
    except:
        pass

# Front-end UI setup
st.title("Security Surveillance")
st.sidebar.text(f"Available cameras: {cams}")
st.sidebar.write("---")
st.sidebar.info("Click to view camera feeds.")

# Security Logs button to view captured images
security_logs = st.sidebar.button("Security Logs")

if security_logs:
    camera_choice = st.sidebar.selectbox("Select Camera", [f"Camera {i+1}" for i in range(cams)])
    
    # Set path for camera logs (images)
    camera_index = int(camera_choice.split()[-1]) - 1
    camera_dir = f"{cap_dir}\\CAMERA{camera_index}"

    # Display images from the selected camera folder
    images = []
    for filename in os.listdir(camera_dir):
        if filename.endswith(".jpg") or filename.endswith(".png"):  # Filter image files
            image_path = os.path.join(camera_dir, filename)
            images.append(image_path)

    if images:
        cols = st.columns(4)  # Display images in a grid (4 images per row)
        for i, image_path in enumerate(images):
            with cols[i % 4]:  # Cycle through columns
                st.image(image_path, caption=f"Image {i+1}", use_column_width=True)
    else:
        st.write("No images found for this camera.")

# Handle page navigation manually
page = st.sidebar.radio("Select Camera Feed", ["Home"] + [f"Camera Feed {i+1}" for i in range(cams)])

if page == "Home":
    st.subheader("Welcome to the Security Surveillance App.")
    st.write("Choose a camera feed to monitor real-time footage.")
else:
    camera_id = int(page.split()[-1]) - 1
    st.subheader(f"Camera {camera_id + 1} Feed")
    # Handle camera feed display here (similar to your base.py logic)
    # For example, use the camera feed capturing logic to show images
    # For simplicity, let's assume you load the camera feed and display images
    st.write(f"Displaying feed from Camera {camera_id + 1}")
