from pytubefix import YouTube
import moviepy.editor as mp
import music_tag
import os



title = "Loyal"
title = "UNLOYAAL"
artist = "ODESZA"
album = "Loyal"
year = 2017
genre = "Electronic"
number = "0"
link = "https://www.youtube.com/watch?v=Sz_YPczxzZc"

yt = YouTube(link)
streams = yt.streams
# print(streams.filter(only_video=True).order_by('resolution').desc().first().download())
print(streams.filter(only_audio=True).order_by("abr").desc().first())
streams.filter(only_audio=True).order_by("abr").desc().first().download(
    filename="Loyal.webm"
)

clip = mp.AudioFileClip("Loyal.webm")
clip.write_audiofile("Loyal.mp3")
clip.close()

os.remove("Loyal.webm")

audiofile = music_tag.load_file("Loyal.mp3")
audiofile['title'] = title
audiofile.save()

