from tkinter import *
import webbrowser
root=Tk()
root.title("Opening hyperlink")
root.iconbitmap("D:\Py_images\calc_icon.png")

def opening():
    webbrowser.open_new(r"www.google.com")
    

button_click=Button(root, text="Click me",command=opening)
button_click.pack()



root.mainloop()
