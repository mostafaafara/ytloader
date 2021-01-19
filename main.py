import tkinter as tk
from tkinter import filedialog
import sys
from pytube import Playlist

#TODO: add exceptions and assync
#TODO: add a cli version
#TODO: make the programe class based

class test:

    def __init__(self):\
        self.inp = sys.argv

    def downloadVid(self,url,dirc):
        pl = Playlist(url)
        count = 0
        for video in pl.videos:
            video.streams.get_lowest_resolution().download(output_path=dirc)
            print(video.title)
            self.listbox.insert(count,video.title)
            count+=1
        print()

    def cli(self):
        dirc = self.inp[self.inp.index("-d")+1]\
            if "-d" in self.inp else "./"
        url = self.inp[self.inp.index("-u")+1]\
            if "-u" in self.inp else exit("url is not specedied")
        self.downloadVid(url,dirc)
 
    def submitHandler(self):
        a = self.url.get()
        print(a)
        self.url.set("")
        self.downloadVid(a,self.dirc)

    def brows(self):
        folder = filedialog.askdirectory()
        self.dirc = folder

    def gui(self):
        label  = tk.Label(self.win,text="Welcome to ytloader").grid(row=0,column=0,columnspan=2)
        label2  = tk.Label(self.win,text="enter your playlist url").grid(row=1,column=0)

        entry = tk.Entry(self.win,textvariable=self.url).grid(row=1,column=1)

        buttonTitle = tk.Label(self.win,text="where you want to save:").grid(row=2,column=0)
        browsbtn = tk.Button(self.win,text="brows",command=self.brows).grid(row=2,column=1)

        listbox = tk.Listbox(self.win,width=30)
        listbox.grid(row=3,column=0,columnspan=2)

        submit = tk.Button(self.win,text="Download",command=self.submitHandler).grid(row=4,column=0,columnspan=2)

        self.win.mainloop()                                

    def main(self):
        if len(self.inp) > 2:
            self.cli()
        else:
            self.win = tk.Tk()

            self.win.title("ytloader")

            self.url = tk.StringVar()
            self.dirc = "./"

            self.gui()
      

if __name__ == "__main__":
    test().main()