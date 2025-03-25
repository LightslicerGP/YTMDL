import cv2
from pytubefix import YouTube

# Initialize YouTube object and get all streams
yt = YouTube("https://youtu.be/YbhunBBpPDs").streams

# Filter out only video streams
video_streams = yt.filter(type="video")

# Find the stream with the highest resolution
highest_res_stream = max(video_streams, key=lambda stream: int(stream.resolution[:-1]))

# Download the highest resolution stream
highest_res_stream.download(filename="downloaded_video.mp4")

# Capture the first frame using cv2
video_capture = cv2.VideoCapture("downloaded_video.mp4")
success, image = video_capture.read()
if success:
    height, width = image.shape[:2]
    size = min(height, width)
    top = (height - size) // 2
    left = (width - size) // 2
    cropped_image = image[top:top+size, left:left+size]
    cv2.imwrite("first_frame.jpg", cropped_image)  # Save the cropped first frame as an image
    print("First frame captured and saved as 'first_frame.jpg'.")
else:
    print("Failed to capture the first frame.")

video_capture.release()
