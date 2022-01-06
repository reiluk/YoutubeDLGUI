# YoutubeDLGUI
A simple GUI for youtube-dl using Tkinter.

![image](https://user-images.githubusercontent.com/92184648/148385686-13af2ca3-d184-4aab-98be-c26693f89746.png)

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
