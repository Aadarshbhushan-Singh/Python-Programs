from tkinter import * 
from PIL import ImageTk,Image
root=Tk()

root.iconbitmap("D:\Py_images\calc_icon.png")

image1=ImageTk.PhotoImage(Image.open("D:\Py_images\house_image.jpg"))
my_label=Label(image=image1)
my_label.pack()


button_quit=Button(root, text="Quit", command=root.quit)
button_quit.pack()

root.mainloop()
