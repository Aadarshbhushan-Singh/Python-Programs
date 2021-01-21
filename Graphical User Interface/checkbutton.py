from tkinter import *
root=Tk()
root.title("Learn Checkbox")
root.iconbitmap("D:\Py_images\calc_icon.png")
root.geometry("400x400")

var=StringVar()
var.set("ON")
c1=Checkbutton(root, text="Checkbutton one", variable=var, onvalue="on", offvalue="off")
#c1.deselect()   This is used for the default deselection of the checkbutton
c1.pack()

label_one=Label(root, text=var.get())
label_one.pack()

def show():
    label_one=Label(root, text=var.get())
    label_one.pack()

button_one=Button(root, text="Click me", command=show)
button_one.pack()

root.mainloop()
