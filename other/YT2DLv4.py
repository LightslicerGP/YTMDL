from pytubefix import Playlist
from moviepy.editor import VideoFileClip
import os

def download_youtube_playlist(playlist_url):
    # Create a playlist object
    playlist = Playlist(playlist_url)
    
    # Iterate through each video in the playlist
    for video in playlist.video_urls:
        try:
            # Get the video object
            yt = Playlist(video)
            
            # Download the highest quality video
            video_stream = yt.streams.get_highest_resolution()
            video_file = video_stream.download()
            
            # Get the title of the video
            title = yt.title
            
            # Convert the video to MP3
            video_clip = VideoFileClip(video_file)
            audio_file = f"{title}.mp3"
            video_clip.audio.write_audiofile(audio_file)
            
            # Delete the original video file
            os.remove(video_file)
            
            print(f"Downloaded: {title}")
        except Exception as e:
            print(f"Error downloading {video}: {str(e)}")

if __name__ == "__main__":
    playlist_url = input("Enter the YouTube playlist URL: ")
    download_youtube_playlist(playlist_url)
