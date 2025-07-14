import cv2
import os

def extract_frames(video_path, output_folder):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Open the video file
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break  # No more frames to read

        # Save frame as image
        frame_filename = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
        cv2.imwrite(frame_filename, frame)

        frame_count += 1

    cap.release()
    print(f"Done: Extracted {frame_count} frames to '{output_folder}'")

# Example usage
video_path = r'D:\other\video to image frame\11.mp4'         # Replace with your video path
output_folder = r'D:\other\video to image frame\output'        # Replace with desired output directory
extract_frames(video_path, output_folder)