
from pytube import Playlist
import streamlit as st
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_single(x):
    audioStream = x.streams.get_by_itag('251')
    audioStream.download(output_path=DOWNLOAD_DIR)

def download_playlist(x):
    print("Number of songs in list: ",len(x.video_urls))
    for video in x.videos:
     audioStream = video.streams.get_by_itag('251')
     audioStream.download(output_path=DOWNLOAD_DIR)


def check_type(x):
    if "watch?" in x:
        return "Single"
    elif "playlist" in x:
        return "playlist"
    else:
        return "error"  
   
root = tk.Tk()
root.withdraw()
root.wm_attributes('-topmost', 1)


st.title("Youtube music downloader")
songs = st.text_input("Enter the song or playlist link")
if songs:
    type = check_type(songs)
    if type == "playlist":
        playlist = Playlist(songs)
        st.subheader(f"You have Entered an playlist Url Named: {playlist.title} It has {len(playlist.video_urls)} songs")
        if st.button("download playlist"):
          DOWNLOAD_DIR = filedialog.askdirectory(master=root)
          download_playlist(playlist)  
    elif type == "Single":
        yt = YouTube(songs)
        st.subheader(f"You have Entered an song Url Named: {yt.title}")
        if st.button("download song"):
            DOWNLOAD_DIR = filedialog.askdirectory(master=root)
            download_single(yt)
    else:
        st.subheader("You have Entered an unsupported URL")
