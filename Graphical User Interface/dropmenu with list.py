from tkinter import *
root=Tk()
root.title("Learn Checkbox")
root.iconbitmap("D:\Py_images\calc_icon.png")
root.geometry("400x400")


clicked=StringVar()
clicked.set("Monday")

days=[
"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"
    ]

dropmenu=OptionMenu(root, clicked, *days)  #use * in front of the name of the list
dropmenu.pack()

def show():
    label_show=Label(root, text=clicked.get())
    label_show.pack()

button_one=Button(root, text="Show selection", command=show)
button_one.pack()


root.mainloop()
