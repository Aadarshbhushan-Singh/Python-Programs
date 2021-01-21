from tkinter import *
from PIL import ImageTk,Image
root=Tk()
root.title("Image Viewer")
root.iconbitmap("D:\Py_images\calc_icon.png")


image_one=ImageTk.PhotoImage(Image.open("D:\Py_images\google_image.png "))
image_two=ImageTk.PhotoImage(Image.open("D:\Py_images\google_image2.png"))
image_three=ImageTk.PhotoImage(Image.open("D:\Py_images\google_image3.jpg"))
image_four=ImageTk.PhotoImage(Image.open("D:\Py_images\google_image4.jpg"))
image_five=ImageTk.PhotoImage(Image.open("D:\Py_images\google_image5.jpg"))
image_six=ImageTk.PhotoImage(Image.open("D:\Py_images\google_image6.jpg"))
image_seven=ImageTk.PhotoImage(Image.open("D:\Py_images\google_image7.png"))
image_eight=ImageTk.PhotoImage(Image.open("D:\Py_images\google_image8.jpg"))

image_list=[image_one, image_two, image_three, image_four, image_five, image_six, image_seven, image_eight]

status=Label(root, text="Image 1 of " + str(len(image_list)), bd=3, relief=SUNKEN, anchor=E)


label_one=Label(image=image_one)
label_one.grid(row=0, column=0, columnspan=3) 

def next_image(image_number):
    if image_number==7:
        button_sakiyo=Button(root, text="Next", state=DISABLED)
        button_sakiyo.grid(row=1, column=2)
        return()
    
    
    global label_one
    global button_next
    global button_previous
    label_one.grid_forget()
    label_one=Label(image=image_list[image_number])
    label_one.grid(row=0, column=0, columnspan=3)
    
   
    
    button_next=Button(root, text="Next", command=lambda: next_image(image_number+1))
    button_next.grid(row=1, column=2)
    button_previous=Button(root, text="Previous", command=lambda: previous_image(image_number-1))
    button_previous.grid(row=1, column=0)

    status=Label(root, text="Image "+str(image_number+1)+" of " + str(len(image_list)), bd=3, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)

    
def previous_image(image_number):
    if image_number<0:
        button_sakiyo=Button(root, text="Previous", state=DISABLED)
        button_sakiyo.grid(row=1, column=0)
        return()
    
    status=Label(root, text="Image " + str(image_number+1)+" of "+str(len(image_list)), bd=2, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W+E)
                
    global label_one
    global button_next
    global button_previous
    label_one.grid_forget()
    label_one=Label(image=image_list[image_number])
    label_one.grid(row=0, column=0, columnspan=3)
    
    button_next=Button(root, text="Next", command=lambda: next_image(image_number+1))
    button_next.grid(row=1, column=2)
    
    button_previous=Button(root, text="Previous", command=lambda: previous_image(image_number-1))
    button_previous.grid(row=1, column=0)
    
    



button_previous=Button(root, text="Previous", state=DISABLED)
button_previous.grid(row=1, column=0)

button_quit=Button(root, text="Quit", command=quit)
button_quit.grid(row=1, column=1)

button_next=Button(root, text="Next", command=lambda: next_image(1))
button_next.grid(row=1, column=2)

status.grid(row=2, column=0, columnspan=3, sticky=W+E)

root.mainloop()
