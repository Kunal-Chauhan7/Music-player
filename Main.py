from tkinter import *
from PIL import Image , ImageTk
class musicplayer:
    def __init__(self , Tk):
        self.root = Tk
        self.root.title('Sugoi Music')
        self.root.geometry("450x400")
        root.configure(background='Sky blue')
        self.bgimg = ImageTk.PhotoImage(file="Imagebg.png")
        photo = Label(self.root,image=self.bgimg).place(x=100,y=20)
root = Tk()
obj = musicplayer(root)
root.mainloop()