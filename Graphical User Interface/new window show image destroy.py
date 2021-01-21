from tkinter import *
from PIL import ImageTk,Image

root=Tk()

root.title("First window")
root.iconbitmap("D:\Py_images\calc_icon.png")


def opentop():
    global image1    #image1 should be decleared global so that button can use this funciton
    top=Toplevel()
    image1=ImageTk.PhotoImage(Image.open("D:\Py_images\google_image.png"))
    Label(top, image=image1).pack()
    top.title("Second window")
    top.iconbitmap("D:\Py_images\calc_icon.png")
    button2=Button(top, text="Destroy", command=top.destroy).pack()

button1=Button(root, text="Open", command=opentop).pack()



root.mainloop()
