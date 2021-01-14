import tkinter as tk
from tkinter import filedialog
from pytube import Playlist

#TODO: add exceptions and assync
#TODO: add a cli version 
#TODO: make the programe class based

win = tk.Tk()

win.title("ytloader")

url = tk.StringVar()
dirc = "./"

def downloadVid(url):

    pl = Playlist(url)
    count = 0
    for video in pl.videos:
        video.streams.get_lowest_resolution().download(output_path=dirc)
        print(video.title)
        listbox.insert(count,video.title)
        count+=1

def submitHandler():
    a = url.get()
    print(a)
    url.set("")
    downloadVid(a)

def brows():
    folder = filedialog.askdirectory()
    global dirc 
    dirc = folder

label  = tk.Label(win,text="Welcome to ytloader").grid(row=0,column=0,columnspan=2)
label2  = tk.Label(win,text="enter your video url").grid(row=1,column=0)

entry = tk.Entry(win,textvariable=url).grid(row=1,column=1)

buttonTitle = tk.Label(win,text="where you want to save:").grid(row=2,column=0)
browsbtn = tk.Button(win,text="brows",command=brows).grid(row=2,column=1)

listbox = tk.Listbox(win,width=30)
listbox.grid(row=3,column=0,columnspan=2)

submit = tk.Button(win,text="Download",command=submitHandler).grid(row=4,column=0,columnspan=2)

win.mainloop()



