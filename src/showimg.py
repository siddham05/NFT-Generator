import os
import tkinter
from tkinter import *
from PIL import Image, ImageTk
import random

files = os.listdir("result/")
out = random.choice(files)
out = "result/" + out

root = tkinter.Tk()
root.title("SAMPLE NFT")
root.after(1,root.focus_force)

img0 = Image.open(out)
fil = ImageTk.PhotoImage(img0)

l0 = tkinter.Label(image = fil)
l0.image = fil
l0.pack()

root.mainloop()