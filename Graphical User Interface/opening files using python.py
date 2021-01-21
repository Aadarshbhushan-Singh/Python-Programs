from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image
root=Tk()
root.title("Open File Dialogue Box")
root.iconbitmap("D:\Py_images\calc_icon.png")

#filetypes=(("key that appers in the small box wherer we select the file","types of the file that should be opened"))
#the default is the first one you list in the filetypes



def openfile():
    global image_1
    root.filename=filedialog.askopenfilename(initialdir="D:\Py_images", title="Opening files", filetypes=(("png files", "*.png"),("all fies","*.*")))
    label_1=Label(root, text=root.filename).pack()
    image_1=ImageTk.PhotoImage(Image.open(root.filename))
    label_image=Label(root, image=image_1)
    label_image.pack()


button1=Button(root, text="open", command=openfile).pack()


root.mainloop()
