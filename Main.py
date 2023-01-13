from tkinter import *
from PIL import Image , ImageTk

from pygame import mixer 
mixer.init()

class musicplayer:
    def __init__(self , Tk):
        def playmusic():
            try:
                Paused
            except NameError:
                try:
                    mixer.music.load("sample.mp3")
                    mixer.music.play()
                    self.labl1['text'] = "Music Playing"
                except:
                    pass
            else:
                mixer.music.unpause()
                self.labl1['text'] = "Music Playing"
        def stopmusic():
            mixer.music.stop()
            self.labl1['text'] = "Music stopped"
        def pausemusic():
            global Paused
            Paused = TRUE
            mixer.music.pause()
            self.labl1['text'] = "Music paused"
        self.root = Tk
        self.root.title('Sugoi Music')
        self.root.geometry("450x400")
        root.configure(background='Sky blue')
        self.bgimg = ImageTk.PhotoImage(file="Imagebg.png")
        photo = Label(self.root,image=self.bgimg).place(x=100,y=40)
        self.msg = "Let's rock☆*: .｡. o(≧▽≦)o .｡.:*☆"
        self.lab = Label(text=self.msg , fg="white" , bg="black").place(x=130 , y=5)
        self.labl1 = Label(self.root,text="Let's play it !!", bg="black" , fg="white")
        self.labl1.pack(side=BOTTOM , fill= X)
        self.playButtonImg = ImageTk.PhotoImage(file="Playbut.png")
        playButton=Button(self.root,image=self.playButtonImg, bd=0 , background="sky blue",command=playmusic).place(x=15 , y=290)
        self.pauseButtonImg = ImageTk.PhotoImage(file="pasuebut.png")
        pauseButton=Button(self.root,image=self.pauseButtonImg, bd=0 , background="sky blue",command=pausemusic).place(x=65 , y=290)
        self.stopButtonImg = ImageTk.PhotoImage(file="Stopbut.png")
        stopButton=Button(self.root,image=self.stopButtonImg, bd=0 , background="sky blue",command=stopmusic).place(x=115 , y=290)

root = Tk()
obj = musicplayer(root)
root.mainloop()