from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox

root=Tk()
root.title("Message Box")
root.iconbitmap("D:\Py_images\calc_icon.png")


#showinfo, showwarning, showerror, askquestin, askokcancel, askyesno

#okcancel returns 1 and 0
#askyesno returns 1 and 0
#askquestion return yes and no
#showerror returns ok
#showwarning returns ok
#showinfo returns ok


def popup():
    answer= messagebox.askyesno("Message Box 1","Hello world")  #The first quote is for title and second for message
    Label(root, text=answer).pack()
    if answer==1:
        Label(root, text="You clicked yes").pack()
    else:
        Labeel(root, text="You clicked No").pack()

Button(root, text="popup", command=popup).pack()





mainloop()
