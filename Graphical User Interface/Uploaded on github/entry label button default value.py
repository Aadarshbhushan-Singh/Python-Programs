from tkinter import *
root=Tk()

e=Entry(root, width=20)
e.pack()
e.insert(0,"Enter your name")

def click():
    hello="Hello"+' '+e.get()+' '+"How are you?"
    label1=Label(root,text=hello)
    #label1=Label(root, text="Hello"+' '+e.get()+' '+"How are you?")
    label1.pack()

button1=Button(root, text="Click Me!",command=click)
button1.pack()

root.mainloop()
