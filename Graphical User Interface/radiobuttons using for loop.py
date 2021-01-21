from tkinter import *
from PIL import ImageTk,Image

root=Tk()


root.title("Adding Frame")
root.iconbitmap("D:\Py_images\calc_icon.png")

cow=StringVar()
cow.set("hi")

list1=[
    ("hello","hi"),
    ("world","world"),
    ("how","how"),
    ("are","are")

    ]
def clicked(value):
    my_label=Label(root, text=value).pack(anchor=W)

for text, value in list1:
    Radiobutton (root, text=text, variable=cow, value=value).pack(anchor=W)

button1=Button(root, text="Click Me", command=lambda: clicked(cow.get())).pack()

mainloop()
