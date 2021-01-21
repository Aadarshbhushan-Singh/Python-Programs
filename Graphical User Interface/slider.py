from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
root=Tk()
root.title("Slider")
root.iconbitmap("D:\Py_images\calc_icon.png")
root.geometry("400x400") 


vertical=Scale(root, from_=0, to=200, bg="blue")
vertical.pack()

horizontal=Scale(root, from_=0, to=200, bg="red", orient=HORIZONTAL)
horizontal.pack()

lebel_vertical=Label(root, text=vertical.get()).pack()

label_horizontal=Label(root,text=horizontal.get())
label_horizontal.pack()

def for_vertical():
    button_vertical=Button(root,text=vertical.get()).pack()
    root.geometry(str(horizontal.get())+ "x" + str(vertical.get()))  

button_vertical=Button(root, text="For Vertical",  command=for_vertical)
button_vertical.pack()

root.mainloop()
