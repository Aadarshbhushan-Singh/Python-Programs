from tkinter import *
import tkinter.font as font
import webbrowser
root=Tk()
root.title("WIKIPEDIA ARTICLES")
root.iconbitmap("D:\Py_images\wikipedia_icon.jpg")


##### First Frame
font_frame_1= font.Font(family='Monotype Corsiva',size=30)

frame_1=LabelFrame(root, text="Articles that you should read",padx=80,pady=50,fg="RED")
frame_1['font'] = font_frame_1
frame_1.grid(row=0, column=0, columnspan=6)

##### Second Frame
font_frame_2=font.Font(family="Monotype Corsiva", size=20)

frame_2=LabelFrame(frame_1, text="Topic of the article", padx=250, pady=150, fg="blue")
frame_2['font']=font_frame_2
frame_2.pack()

#### Third frame
frame_3=LabelFrame(frame_2)
frame_3.pack()

def openlink(topic_number):
    if topic_number==1:
        webbrowser.open_new(r"https://en.wikipedia.org/wiki/A._P._J._Abdul_Kalam")
    elif topic_number==2:
        webbrowser.open_new(r"https://en.wikipedia.org/wiki/Donald_Trump")
    elif topic_number==3:
        webbrowser.open_new(r"https://en.wikipedia.org/wiki/Barack_Obama")
    elif topic_number==4:
        webbrowser.open_new(r"https://simple.wikipedia.org/wiki/Narendra_Modi")
    elif topic_number==5:
        webbrowser.open_new(r"https://en.wikipedia.org/wiki/Nelson_Mandela")

        
list_topic=[
"A.P.J Abdul Kalam",
"Donald Trump",
"Barack Obama",
"Narendra Modi",
"Nelson Mandela",

    ]
def next_button(topic_number):
    global label_topic_1
    global button_next
    global button_back
    
    if topic_number==6:
        button_next=Button(root, text="Next", padx=50, pady=10, fg="blue", state=DISABLED, font=('Helvetica', 15, 'bold'))
        button_next.grid(row=1, column=3)
        return()

    label_topic_1.destroy()
    label_topic_1=Label(frame_3, text="Biography of "+list_topic[topic_number-1], font=('Helvetica', 18, 'bold'))
    label_topic_1.pack()
    topic_number=topic_number+1

    button_next=Button(root, text="Next", padx=50, pady=10, fg="blue", command=lambda: next_button(topic_number), font=('Helvetica', 15, 'bold'))
    button_next.grid(row=1, column=3)

    button_read=Button(root, text="Read", padx=50, pady=10, fg="blue", command=lambda: openlink(topic_number-1), font=('Helvetica', 15, 'bold'))
    button_read.grid(row=1, column=2)

    button_back=Button(root, text="Back", padx=50, pady=10, fg="blue",command=lambda: back_button(topic_number-3), font=('Helvetica', 15, 'bold'))
    button_back.grid(row=1, column=0)

    button_quit=Button(root, text="Quit", padx=50, pady=10, fg="red", command=quit, font=('Helvetica', 15, 'bold'))
    button_quit.grid(row=1, column=4)

    status=Label(root, text="Article "+str(topic_number-1)+ " of "+str(len(list_topic)), fg="purple", font=('Helvetica', 18, 'bold'))
    status.grid(row=2, column=0)

def back_button(topic_number):
    global label_topic_1
    global button_next
    global button_back

    if topic_number==-1:
        button_back=Button(root, text="Back", padx=50, pady=10, fg="blue", state=DISABLED, font=('Helvetica', 15, 'bold'))
        button_back.grid(row=1, column=0)
        return()
    
    label_topic_1.destroy()
    label_topic_1=Label(frame_3, text="Biography of "+list_topic[topic_number], font=('Helvetica', 18, 'bold'))
    label_topic_1.pack()
    topic_number=topic_number-1

    button_back=Button(root, text="Back", padx=50, pady=10, fg="blue",command=lambda: back_button(topic_number), font=('Helvetica', 15, 'bold'))
    button_back.grid(row=1, column=0)

    button_read=Button(root, text="Read", padx=50, pady=10, fg="blue", command=lambda: openlink(topic_number+2), font=('Helvetica', 15, 'bold'))
    button_read.grid(row=1, column=2)

    button_next=Button(root, text="Next", padx=50, pady=10, fg="blue", command=lambda: next_button(topic_number+3), font=('Helvetica', 15, 'bold'))
    button_next.grid(row=1, column=3)

    button_quit=Button(root, text="Quit", padx=50, pady=10, fg="red", command=quit, font=('Helvetica', 15, 'bold'))
    button_quit.grid(row=1, column=4)

    status=Label(root, text="Article "+str(topic_number+2)+ " of "+str(len(list_topic)), fg="purple", font=('Helvetica', 18, 'bold'))
    status.grid(row=2, column=0)
    


label_topic_1=Label(frame_3, text="Biography of A.P.J Abdul Kalam", font=('Helvetica', 18, 'bold'))
label_topic_1.pack()

button_back=Button(root, text="Back", padx=50, pady=10, fg="blue", state=DISABLED, font=('Helvetica', 15, 'bold'))
button_back.grid(row=1, column=0)

button_read=Button(root, text="Read", padx=50, pady=10, fg="blue", command=lambda: openlink(1), font=('Helvetica', 15, 'bold'))
button_read.grid(row=1, column=2)

button_next=Button(root, text="Next", padx=50, pady=10, fg="blue", command=lambda: next_button(2), font=('Helvetica', 15, 'bold'))
button_next.grid(row=1, column=3)

button_quit=Button(root, text="Quit", padx=50, pady=10, fg="red", command=quit, font=('Helvetica', 15, 'bold'))
button_quit.grid(row=1, column=4)

status=Label(root, text="Article 1 of "+str(len(list_topic)), fg="purple", font=('Helvetica', 15, 'bold'))
status.grid(row=2, column=0)

root.mainloop()
