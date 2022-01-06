# YoutubeDLGUI
A simple GUI for youtube-dl using Tkinter.

![image](https://user-images.githubusercontent.com/92184648/148385164-76a129d4-3466-4818-8b4e-6c0ccf0bb8fa.png)

## Installation
    git clone https://github.com/reiluk/YoutubeDLGUI/
### Dependencies
    cd YoutubeDLGUI
    pip install -r requirements.txt
or
    
    pip install youtube_dl
    pip install ttkthemes
### FFmpeg
YoutubeDLGUI requires a FFmpeg installation for converting the download to MP3/MP4.
Download FFmpeg from https://www.ffmpeg.org/download.html and add the directory containing the FFmpeg binaries to your PATH environment variable.

Alternatively, you can specify the path of your FFmpeg installation in "YoutubeDLGUI.py" (line 42 and 54).
For Instance:

    "ffmpeg_location": "C:/ffmpeg",
    
## Usage
Run "YoutubeDLGUI.py".
    
    python YoutubeDLGUI.py
