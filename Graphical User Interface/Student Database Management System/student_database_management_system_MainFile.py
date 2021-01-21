#Frontend
from tkinter import *
import tkinter.messagebox
class student:
	def __init__(self, root):
		self.root=root
		self.root.title("Student Databse Management System")
		self.root.geometry('1350x750+0+0')
		self.root.config(bg="Cadet blue")

if __name__=='__main__':
	root=Tk()
	application=student(root)
	root.mainloop()