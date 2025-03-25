import os
import pytube
from moviepy.editor import VideoFileClip
from PIL import Image
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, TIT2, TPE1, TALB, COMM

def convert(playlist_url):
    playlist = pytube.Playlist(playlist_url)
    for video in playlist.videos:
        video_path = download_current_video(video)
        audio_path = convert_video_to_audio(video_path)
        print(f"Converted video to audio: {video.title}")

def download_current_video(video):
    output_path = "Result"
    os.makedirs(output_path, exist_ok=True)
    video_path = video.streams.get_highest_resolution().download(output_path=output_path)
    print(f"Downloaded video: {video.title}")
    return video_path

def convert_video_to_audio(video_path):
    audio_path = os.path.splitext(video_path)[0] + ".mp3"
    video = VideoFileClip(video_path)
    
    # Extract the first frame of the video
    frame = video.get_frame(0)
    
    # Write the frame as the audio file's album cover
    cover_path = os.path.splitext(video_path)[0] + ".jpg"
    frame_image = Image.fromarray(frame)
    frame_image.save(cover_path, "JPEG")
    
    # Extract audio and set the album cover and metadata
    audio = video.audio
    audio.write_audiofile(audio_path, codec="mp3")
    
    # Set metadata for the audio file
    audio_file = MP3(audio_path, ID3=ID3)
    audio_file.tags.add(APIC(3, 'image/jpeg', 3, 'Front cover', open(cover_path, 'rb').read()))
    audio_file.tags.add(TIT2(encoding=3, text='Audio Title'))
    audio_file.tags.add(TPE1(encoding=3, text='Artist Name'))
    audio_file.tags.add(TALB(encoding=3, text='Album Name'))
    audio_file.tags.add(COMM(encoding=3, lang='eng', desc='desc', text='Description'))
    audio_file.save()
    
    # Clean up the temporary cover image file
    os.remove(cover_path)
    
    return audio_path


# Example usage
playlist_url = 'https://www.youtube.com/playlist?list=PLG5Wd810mzkqNOoh-bK5j7pkS-wZew2-v'
convert(playlist_url)
