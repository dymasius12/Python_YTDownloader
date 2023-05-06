#!/opt/anaconda3/bin/python
from pytube import YouTube

link = input("link:")
yt = YouTube(link, use_oauth=True, allow_oauth_cache=True)
yt.streams.get_highest_resolution().download('./downloaded')
print("downloaded")
