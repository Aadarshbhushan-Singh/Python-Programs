from tkinter import *
root =Tk()

root.title("aaddarsh ko calculator")

e=Entry(root, width=50, borderwidth=5)
e.grid(row=0, column=0, columnspan=3)

def click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current)+str(number))

def clear():
    e.delete(0,END)

def addition():
    first_number=e.get()
    global f_num
    global math
    math='addition'
    f_num=int(first_number)
    e.delete(0,END)

def subtraction():
    first_number=e.get()
    global f_num
    global math
    math='subtraction'
    f_num=int(first_number)
    e.delete(0,END)

def multiplication():
    first_number=e.get()
    global f_num
    global math
    f_num=int(first_number)
    math='multiplication'
    e.delete(0,END)
def division():
    first_number=e.get()
    global f_num
    global math
    f_num=int(first_number)
    math='division'
    e.delete(0,END)

def equal():
    second_number=e.get()
    e.delete(0,END)
    
    if math=='addition':
        e.insert(0, (f_num+int(second_number)))
        
    elif math=='subtraction':
        e.insert(0, (f_num-int(second_number)))
                 
    elif math=='multiplication':
        e.insert(0, (f_num*int(second_number)))
        
    elif math=='division':
        e.insert(0, (f_num/int(second_number)))
    
    

button_1=Button(root, text='1', padx=45,pady=25, command= lambda: click(1))
button_1.grid(row=1,column=0)

button_2=Button(root, text='2', padx=45,pady=25, command= lambda: click(2))
button_2.grid(row=1,column=1)

button_3=Button(root, text='3', padx=45,pady=25, command= lambda: click(3))
button_3.grid(row=1,column=2)

button_4=Button(root, text='4', padx=45, pady=25, command= lambda: click(4))
button_4.grid(row=2, column=0)

button_5=Button(root, text='5', padx=45, pady=25, command= lambda: click(5))
button_5.grid(row=2, column=1)

button_6=Button(root, text='6', padx=45, pady=25, command= lambda: click(6))
button_6.grid(row=2, column=2)

button_7=Button (root, text='7', padx=45, pady=25,command= lambda: click(7))
button_7.grid(row=3, column=0)

button_8=Button(root, text='8', padx=45, pady=25, command= lambda: click(8))
button_8.grid(row=3,column=1)

button_9=Button(root, text='9', padx=45, pady=25, command= lambda: click(9))
button_9.grid(row=3, column=2)

button_0=Button(root, text='0', padx=45, pady=25, command= lambda: click(0))
button_0.grid(row=4, column=0)

button_clear=Button(root, text='clear', padx=45, pady=25,command=clear)
button_clear.grid(row=4, column=1)

button_plus=Button(root, text='+', padx=45, pady=25, command=addition)
button_plus.grid(row=4, column=2)

button_sub=Button(root, text='-', padx=45, pady=25,command=subtraction)
button_sub.grid(row=5, column=0)

button_multiply=Button(root, text='*', padx=45, pady=25,command=multiplication)
button_multiply.grid(row=5, column=1)

button_divide=Button(root, text='/', padx=45, pady=25, command=division)
button_divide.grid(row=5, column=2)

button_equal=Button(root, text='=', padx=45, pady=25, command=equal)
button_equal.grid(row=6, column=2)




root.mainloop()
