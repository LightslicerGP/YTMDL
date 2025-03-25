import os
from pytube import Playlist, YouTube
from moviepy.editor import VideoFileClip

def download_video_as_mp3(video_url, output_folder):
    youtube = YouTube(video_url)
    video = youtube.streams.filter(only_audio=True).first()
    video_path = video.download(output_path=output_folder)

    audio_path = os.path.splitext(video_path)[0] + ".mp3"
    video_clip = VideoFileClip(video_path)
    audio = video_clip.audio
    audio.write_audiofile(audio_path, codec='mp3')
    audio.close()
    video_clip.close()
    
    # Clean up the temporary video file
    os.remove(video_path)

    return audio_path

def download_playlist_as_mp3(playlist_url, output_folder):
    playlist = Playlist(playlist_url)
    for video_url in playlist.video_urls:
        audio_file = download_video_as_mp3(video_url, output_folder)
        print(f"Downloaded and converted to MP3: {os.path.basename(audio_file)}")

# Example usage
playlist_url = 'https://www.youtube.com/playlist?list=PLG5Wd810mzkrYAGBKB4ZafD_EsN-D2coQ'
output_folder = 'Result'
download_playlist_as_mp3(playlist_url, output_folder)
