from tkinter import *
from PIL import ImageTk,Image

root=Tk()


root.title("Adding Frame")
root.iconbitmap("D:\Py_images\calc_icon.png")

frame1=LabelFrame(root, text="Hello world.....", padx=10, pady=10)#padx,y here is for inside of the frame
frame1.pack(padx=50,pady=50) #pack puts the frame in root, so this padx,y is for outside of the frame


b1=Button(frame1, text="Button 1") #pack the button in frame not in the root
b1.grid(row=0, column=0)
b2=Button(frame1, text="Button 2")
b2.grid(row=1, column=1)

root.mainloop()
