from tkinter import *
from PIL import ImageTk,Image

root=Tk()

root.title("First window")
root.iconbitmap("D:\Py_images\calc_icon.png")

top=Toplevel()
image1=ImageTk.PhotoImage(Image.open("D:\Py_images\google_image.png"))
Label(top, image=image1).pack()
top.title("Second window")
top.iconbitmap("D:\Py_images\calc_icon.png")


root.mainloop()
