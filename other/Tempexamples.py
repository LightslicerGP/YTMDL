

# downloadedVid = video.streams.get_audio_only()
# downloadedVid.download(output_path=folder,mp3=True)

# if "(" in title:
#     title = title.split("(")[0]

# isSingle = False
# if " - Single" in ITalbum:
#     isSingle = True

# print("Artist:", ITartist)
# print("Date Published:", ITdate_published)
# print("Album:", ITalbum)


# first frame
# from pytube import YouTube
# import cv2

# def download_youtube_thumbnail(youtube_url, output_file):
#     try:
#         # Download the YouTube video
#         yt = YouTube(youtube_url)
#         video_stream = yt.streams.first()
#         video_stream.download(filename='temp_video')

#         # Capture the first frame
#         cap = cv2.VideoCapture('temp_video.mp4')
#         ret, frame = cap.read()
#         if ret:
#             cv2.imwrite(output_file, frame)
#             print("Thumbnail saved successfully!")
#         else:
#             print("Failed to capture the first frame.")

#         # Clean up temporary files
#         cap.release()
#         cv2.destroyAllWindows()
#         os.remove('temp_video.mp4')
#     except Exception as e:
#         print("An error occurred:", e)

# # Example usage
# youtube_link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Example YouTube link
# output_file = "thumbnail.jpg"  # Output file name

# download_youtube_thumbnail(youtube_link, output_file)


# cover art
# import eyed3

# def set_mp3_album_cover(mp3_file, cover_image):
#     audiofile = eyed3.load(mp3_file)

#     # Open the cover image file
#     with open(cover_image, "rb") as f:
#         cover_data = f.read()

#     # Set the album/song cover art
#     audiofile.tag.images.set(
#         type_=3,  # Image type: 3 for cover (front)
#         img_data=cover_data,
#         mime_type="image/jpeg"  # Adjust mime type if your image format is different
#     )
#     audiofile.tag.save()

#     print("Album cover set successfully!")

# # Example usage
# mp3_file = "example.mp3"  # Path to your MP3 file
# cover_image = "cover.jpg"  # Path to your cover image file

# set_mp3_album_cover(mp3_file, cover_image)

# song data from itunes
# import requests

# def get_song_info(song_name):
#     # Replace spaces in song name with '+'
#     query = song_name.replace(' ', '+')

#     # iTunes Search API URL
#     url = f"https://itunes.apple.com/search?term={query}&entity=song"

#     # Make the request to the iTunes Search API
#     response = requests.get(url)
#     data = response.json()

#     # Check if there are results
#     if data['resultCount'] == 0:
#         print("No results found.")
#         return

#     # Extract relevant information from the first result
#     first_result = data['results'][0]
#     artist = first_result['artistName']
#     date_published = first_result['releaseDate']
#     album = first_result['collectionName']

#     print("Artist:", artist)
#     print("Date Published:", date_published)
#     print("Album:", album)

# # Example usage
# song_name = "Shape of You"  # Example song name
# get_song_info(song_name)


# setting author
# import eyed3

# def set_mp3_author(mp3_file, new_author):
#     audiofile = eyed3.load(mp3_file)
#     audiofile.tag.artist = new_author
#     audiofile.tag.save()

#     print("Author set successfully!")

# # Example usage
# mp3_file = "example.mp3"  # Path to your MP3 file
# new_author = "New Author"  # New author name

# set_mp3_author(mp3_file, new_author)


# setting published year
# import eyed3

# def set_published_year(mp3_file, published_year):
#     audiofile = eyed3.load(mp3_file)

#     # Set the published year
#     audiofile.tag.release_date = str(published_year)
#     audiofile.tag.save()

#     print("Published year set successfully!")

# # Example usage
# mp3_file = "example.mp3"  # Path to your MP3 file
# published_year = 2022  # Published year

# set_published_year(mp3_file, published_year)


# importing a json
# import json

# def load_json_file(file_path):
#     with open(file_path, 'r') as file:
#         data = json.load(file)
#     return data

# # Example usage
# json_file_path = 'data.json'
# data_dict = load_json_file(json_file_path)
# print(data_dict)


# seeing if given data is an entry in a json
# import json

# def check_entry(json_file, entry):
#     with open(json_file, 'r') as file:
#         data = json.load(file)
#         if entry in data:
#             print("Pass")
#         else:
#             print("Fail")

# # Example usage
# json_file = 'your_file.json'  # Replace with the path to your JSON file
# entry_to_check = 'Loyal Odesza'

# check_entry(json_file, entry_to_check)


# using a link to open an image
# import requests
# from PIL import Image
# from io import BytesIO

# def download_and_open_image(image_url):
#     # Download the image
#     response = requests.get(image_url)
#     if response.status_code == 200:
#         # Open the image using PIL
#         img = Image.open(BytesIO(response.content))
#         img.show()  # Open the image using the default image viewer
#     else:
#         print("Failed to download the image")

# # Example usage
# image_url = "https://example.com/image.jpg"  # Replace with your image URL
# download_and_open_image(image_url)


# download image from a certain time on a video
# from pytube import YouTube
# from moviepy.editor import *

# def download_video_screenshot(youtube_url, time_seconds, output_file):
#     try:
#         # Download the YouTube video
#         yt = YouTube(youtube_url)
#         video_stream is yt.streams.filter(progressive=True, file_extension='mp4').first()
#         video_stream.download(filename='temp_video')

#         # Extract a screenshot at the specified time
#         video_clip = VideoFileClip('temp_video.mp4')
#         screenshot = video_clip.get_frame(time_seconds)
#         video_clip.close()

#         # Save the screenshot
#         screenshot_img = Image.fromarray(screenshot)
#         screenshot_img.save(output_file)

#         print("Screenshot saved successfully!")
#     except Exception as e:
#         print("An error occurred:", e)

# # Example usage
# youtube_link = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"  # Example YouTube link
# time_seconds = 2  # Time in seconds to capture the screenshot
# output_file = "screenshot.jpg"  # Output file name

# download_video_screenshot(youtube_link, time_seconds, output_file)
