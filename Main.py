from tkinter import *
from PIL import Image , ImageTk
class musicplayer:
    def __init__(self , Tk):
        self.root = Tk
        self.root.title('Sugoi Music')
        self.root.geometry("450x400")
        root.configure(background='Sky blue')
        self.bgimg = ImageTk.PhotoImage(file="Imagebg.png")
        photo = Label(self.root,image=self.bgimg).place(x=100,y=40)
        self.msg = "Let's rock☆*: .｡. o(≧▽≦)o .｡.:*☆"
        self.lab = Label(text=self.msg , fg="white" , bg="black").place(x=130 , y=5)
        self.labl1 = Label(self.root,text="Let's play it !!")
        self.labl1.pack(side=BOTTOM , fill= X)
        self.playButtonImg = ImageTk.PhotoImage(file="Playbut.png")
        playButton=Button(self.root,image=self.playButtonImg, bd=0 , background="sky blue").place(x=15 , y=290)
        self.pauseButtonImg = ImageTk.PhotoImage(file="pasuebut.png")
        pauseButton=Button(self.root,image=self.pauseButtonImg, bd=0 , background="sky blue").place(x=65 , y=290)
        self.stopButtonImg = ImageTk.PhotoImage(file="Stopbut.png")
        stopButton=Button(self.root,image=self.stopButtonImg, bd=0 , background="sky blue").place(x=115 , y=290)

root = Tk()
obj = musicplayer(root)
root.mainloop()