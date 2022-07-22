from pytube import YouTube
from pathlib import Path
from tkinter import *
from io import BytesIO

def show_end_message():
    finish_message = Label(root, text="Download has completed", bg="dark grey")
    finish_message.pack()
    finish_message.after(3000, lambda: finish_message.destroy() )

def retrieve_input():
    youtube_link=inputtxt.get("1.0","end-1c")
    download_method = clicked.get()
    print('download option is ' + download_method)
    print('url is ' + youtube_link)

    yt = YouTube(youtube_link)
    print("Title of the video is : " + yt.title)

    if download_method == 'Download a video':
        yd = yt.streams.get_highest_resolution()

        yd.download(downloads_path)

        print('File has been saved here ' + downloads_path)
        show_end_message()
    elif download_method == 'Extract audio':

        audio = yt.streams.filter(only_audio=True, file_extension='mp4').first()
        audio.download(downloads_path)
        print('Download of the audio Completed and saved here ' + downloads_path)
        show_end_message()

downloads_path = str(Path.home() / "Downloads")

# create a GUI window
root = Tk()

# set the background colour of GUI window
root.configure(background='light grey')

# set the title of GUI window
root.title("Download from youtube")

# set the configuration of GUI window
root.geometry("500x500")
# create a Form label
heading = Label(root, text="Select if you want to download the video or extract the audio", bg="dark grey")
heading.pack()

choices=['Download a video', 'Extract audio']
clicked = StringVar()
clicked.set(choices[0])

drop = OptionMenu(root, clicked, *choices)
drop.pack()

# Take an user input
# TextBox Creation
url_explain = Label(root, text="Paste the url of the Youtube video", bg="dark grey")
url_explain.pack()
inputtxt = Text(root,
                   height = 5,
                   width = 60)
inputtxt.pack()

buttonCommit=Button(root, height=1, width=10, text="Download", 
                    command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()

# start the GUI
root.mainloop()