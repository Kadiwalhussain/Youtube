import yt_dlp

url1 = input("Enter Video Url: ")

ydl_opts = {}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Video Downloaded successfully!")
