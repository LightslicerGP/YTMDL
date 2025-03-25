from pytube import YouTube
path = "../Result" # substitute to where you want to place the downloaded file

def YTDownload(link):
    youTubeObject = YouTube(link)
    youTubeObject = youTubeObject.streams.get_highest_resolution()
    try:
        if youTubeObject is not None:
            youTubeObject.download(path)
    except:
        print("There has been an error.")
    
    print("All good.")
    
link = input("What video URL? ")
YTDownload(link)