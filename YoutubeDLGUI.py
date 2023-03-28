from tkinter import ttk
from tkinter import filedialog
import yt_dlp
from ttkthemes import ThemedTk
import tkinter as tk
import threading
import os

filename = os.getcwd()
progress = ""


def browse_button():
    global folder_path
    global filename
    filename = filedialog.askdirectory()
    folder_path.set(filename)


def threadmanager():
    t = threading.Thread(target=started)
    t.start()


def my_hook(d):
    global progress
    if d["status"] == "downloading":
        progress = "Progress:" + d["_percent_str"].replace("\x1b[0;94m", "").replace("\x1b[0m", "") + "  Speed: " + d["_speed_str"].replace("\x1b[0;32m", "").replace("\x1b[0m", "")
    elif d["status"] == "finished":
        progress = "Finished downloading!"
    msg.config(text=progress)
    msg.pack()


def started():
    error.config(text="OK!")
    error.pack()
    try:
        if selected.get() == 1:
            ydl_options = {"format": "bestaudio",
                           "outtmpl": str(filename) + "/%(title)s" + ".%(ext)s",
                           #"ffmpeg_location": "C:/ffmpeg",
                           "progress_hooks": [my_hook],
                           "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "mp3"}]}
            if input.get().count(".com") == 1:
                with yt_dlp.YoutubeDL(ydl_options) as ydl:
                    ydl.download([input.get()])
            else:
                with yt_dlp.YoutubeDL(ydl_options) as ydl:
                    ydl.download([f"ytsearch:{input.get()}"])
        elif selected.get() == 2:
            ydl_options = {"format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]",
                           "outtmpl": str(filename) + "/%(title)s" + ".%(ext)s",
                           #"ffmpeg_location": "C:/ffmpeg",
                           "progress_hooks": [my_hook]}
            if input.get().count(".com") == 1:
                with yt_dlp.YoutubeDL(ydl_options) as ydl:
                    ydl.download([input.get()])
            else:
                with yt_dlp.YoutubeDL(ydl_options) as ydl:
                    ydl.download([f"ytsearch:{input.get()}"])
        else:
            error.config(text="Select a format!")
    except yt_dlp.utils.DownloadError:
        error.config(text="Title or URL missing!")
    error.pack()


root = ThemedTk(theme="arc")
root.title("Youtube-DL")
root.geometry("300x220")
root.minsize(300, 220)
root.maxsize(300, 220)
title = ttk.Label(root, text="Youtube-DL GUI")
title.pack()
title = ttk.Label(root, text="Title or URL:")
title.pack()
input = ttk.Entry(root, width=45)
input.pack()
selected = tk.IntVar()
MP3 = ttk.Radiobutton(root, text="MP3", value=1, variable=selected)
MP4 = ttk.Radiobutton(root, text="MP4", value=2, variable=selected)
MP3.pack()
MP4.pack()
folder_path = tk.StringVar()
folder_path.set(filename)
br = ttk.Label(root, textvariable=folder_path)
br.pack()
br2 = ttk.Button(text="Browse", command=browse_button)
br2.pack()
msg = ttk.Label(root, text="")
error = ttk.Label(root, text="")
btn = ttk.Button(root, text="Download", command=threadmanager)
btn.pack()
root.mainloop()
