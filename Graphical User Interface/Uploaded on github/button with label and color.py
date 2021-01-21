from tkinter import *
root=Tk()


def blue():
    label1=Label(root, text="This is blue color", fg="blue")
    label1.pack()
def red():
    label2=Label(root, text="This is red color", fg="red")
    label2.pack()
def green():
    label3=Label(root, text="This is green color", fg="green")
    label3.pack()

button1=Button(root, text="Click Me!", fg="blue",padx=20,pady=20,command=blue)
button2=Button(root, text="Click Me!", fg="red",padx=20,pady=20,command=red)
button3=Button(root, text="Click Me!", fg="green",padx=20,pady=20,command=green)

button1.pack()
button2.pack()
button3.pack()

root.mainloop()
