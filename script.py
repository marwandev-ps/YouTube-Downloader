#importing files
from pytube import YouTube
import cv2

#input video link and Path
Vlink = input("Enter Video Link: ")
VPAth  = input("Enter The Path of The Download: ")
video = YouTube(Vlink)
#print video descriptions

print(f"Title: {video.title}")
print(f"Length: {float(video.length / 60)} min")
print(f"Views: {video.views}")

#set resolution
videoStream = video.streams.get_highest_resolution()

#Download
print("Downloading....")
videoStream.download(VPAth)
print("Downloading finished!!")
#quit
quit()

