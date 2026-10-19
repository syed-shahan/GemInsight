import cv2
import os

# Video path
video_path = "videos/moissanate.mp4"
output_folder = "dataset/moissanate"

# Create folder if not exists
os.makedirs(output_folder, exist_ok=True)

# Load video
cap = cv2.VideoCapture(video_path)

count = 0
saved = 0

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Save every 5th frame
    if count % 5 == 0:
        filename = f"{output_folder}/img_{saved}.jpg"
        cv2.imwrite(filename, frame)
        saved += 1

    count += 1

cap.release()

print("Done extracting images!")