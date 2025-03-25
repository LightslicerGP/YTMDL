import os
import pytube
import re
from mutagen import File
from mutagen.id3 import ID3, APIC

def download_youtube_playlist(url):
    playlist = pytube.Playlist(url)
    for video_url in playlist.video_urls:
        try:
            video = pytube.YouTube(video_url)
            audio = video.streams.filter(only_audio=True).first()
            audio.download(output_path='temp')
        except Exception as e:
            print(f"Error downloading video: {video_url}")
            print(e)

def extract_album_cover(video_url, output_path):
    try:
        video = pytube.YouTube(video_url)
        thumbnail_url = video.thumbnail_url
        thumbnail_path = os.path.join(output_path, 'temp.jpg')
        pytube.helpers.download_url(thumbnail_url, filename=thumbnail_path)
        return thumbnail_path
    except Exception as e:
        print(f"Error extracting album cover for video: {video_url}")
        print(e)
        return None

def apply_album_cover(audio_path, cover_path):
    cover = open(cover_path, 'rb').read()
    audio = File(audio_path, easy=True)
    audio['APIC'] = APIC(
        encoding=3,
        mime='image/jpeg',
        type=3,  # Front cover
        desc=u'Cover',
        data=cover
    )
    audio.save()

# Example usage
playlist_url = 'https://www.youtube.com/playlist?list=PLG5Wd810mzkqNOoh-bK5j7pkS-wZew2-v'
output_folder = 'Result'

download_youtube_playlist(playlist_url)
os.makedirs(output_folder, exist_ok=True)
for file in os.listdir('temp'):
    if file.endswith('.mp4'):
        audio_path = os.path.join('temp', file)

        video_id = file.split('.')[0]
        video_url = f'https://www.youtube.com/watch?v={video_id}'
        album_cover_path = extract_album_cover(video_url, output_folder)

        if album_cover_path:
            apply_album_cover(audio_path, album_cover_path)

            os.rename(audio_path, os.path.join(output_folder, f'{video_id}.mp3'))

            os.remove(album_cover_path)
os.rmdir('temp')
