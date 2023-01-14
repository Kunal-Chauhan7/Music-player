from tkinter import *
from PIL import Image , ImageTk

from pygame import mixer 
mixer.init()

class musicplayer:
    def __init__(self , Tk):
        def mute():
            mixer.music.set_volume(0)
            self.mutes = Button(self.root,image=self.mute,bd=0, command=unmute , background="sky blue").place(x=220,y=300)
        def unmute():
            mixer.music.set_volume(0.25)
            volumeStatus = Button(self.root,image=self.unmute,command=mute,bd=0 , background="sky blue").place(x=220,y=300)
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
        def volumefun(vol):
            volume = int(vol)/100
            mixer.music.set_volume(volume)
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
        self.labl2 = Label(self.root,text="Volume",fg="black",bg="sky blue",font='Helvetica 10 bold')
        self.labl2.place(x=270,y=280)
        self.volume = Scale(self.root,from_=0,to=100,orient=HORIZONTAL,bg="light grey" , length=160,bd=0,command=volumefun)
        self.volume.place(x=270,y=300)
        self.volume.set(25)
        self.unmute = ImageTk.PhotoImage(file="unmute.png")
        self.mute = ImageTk.PhotoImage(file="mute.png")
        volumeStatus = Button(self.root,image=self.unmute,command=mute,bd=0 , background="sky blue").place(x=220,y=300)
root = Tk()
obj = musicplayer(root)
root.mainloop()