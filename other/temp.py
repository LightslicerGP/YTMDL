from pytubefix import YouTube
from moviepy.editor import *
from PIL import Image


def download_video_screenshot(youtube_url, time_seconds, output_file):
    try:
        # Download the YouTube video
        yt = YouTube(youtube_url)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(filename="temp_video.mp4")

        # Extract a screenshot at the specified time
        video_clip = VideoFileClip("temp_video.mp4")
        screenshot = video_clip.get_frame(time_seconds)
        video_clip.close()

        # Save the screenshot
        screenshot_img = Image.fromarray(screenshot)
        screenshot_img.save(output_file, format="png")

        print("Screenshot saved successfully!")
    except Exception as e:
        print("An error occurred:", e)


# Example usage
youtube_link = "https://www.youtube.com/watch?v=Sz_YPczxzZc"  # Example YouTube link
time_seconds = 0  # Time in seconds to capture the screenshot
output_file = "screenshot.jpg"  # Output file name

download_video_screenshot(youtube_link, time_seconds, output_file)
