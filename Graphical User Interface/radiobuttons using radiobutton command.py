from tkinter import *
from PIL import ImageTk,Image

root=Tk()


root.title("Adding Frame")
root.iconbitmap("D:\Py_images\calc_icon.png")

r=IntVar()#if string is passed in value like [value="1"], then StringVar is used instead of IntVar()
r.set("1")

def clicked(value):
     my_label=Label(root, text=value)
     my_label.pack()

Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text="Option 2", variable=r, value=2,command=lambda: clicked (r.get())).pack()

my_label=Label(root, text=r.get())
my_label.pack()

button1=Button(root, text="Click Me", command=lambda: clicked (r.get())).pack()

mainloop()
