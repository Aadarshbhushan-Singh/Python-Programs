from tkinter import *
from tkinter import messagebox
import os
root=Tk()

#---------------------------------  Registeration -------------------------------------------------#

def register():
	root1=Tk()
	root1.title("Form creating and linkint with database.")
	root1.geometry("500x500")

	def register_username():
		username_info=entry_username.get()
		password_info=entry_password.get()

		file=open(username_info,"w")   #username_info here is a variable. You can keep the name of file constant also. 'NameOfFile'
		file.write(username_info+"\n")
		file.write(password_info)
		file.close()

		entry_username.delete(0, END)
		entry_password.delete(0, END)

		label_success=Label(root1, text="Registeration successful!", fg="green")
		label_success.pack()

	username=StringVar()
	password=StringVar()

	label2=Label(root1, text="Please enter the details below.")
	label2.pack()

	label_username=Label(root1, text="Username *")
	label_username.pack()
	entry_username=Entry(root1, textvariable=username)
	entry_username.pack()

	label_password=Label(root1, text="Password *")
	label_password.pack()
	entry_password=Entry(root1, textvariable=password)
	entry_password.pack()

	label_blank=Label(root1, text="").pack()

	button_register2=Button(root1, text="Register", width="15", height="2", command=register_username)
	button_register2.pack()
	root1.mainloop()

#---------------------------------  Login Function -------------------------------------------------#
def login_function():
	root2=Tk()
	root2.title("Login Form")
	root2.geometry("500x500")

	def login_verify():
		username1=username_entry1.get()
		password1=password_entry1.get()

		username_entry1.delete(0, END)
		password_entry1.delete(0, END)

		list_of_files=os.listdir()
		if username1 in list_of_files:
			file1=open(username1, "r")
			verify=file1.read().splitlines()
			if password1 in verify:
				messagebox.showinfo("Login Successful","Login Successful")
			else:
				messagebox.showerror("Wrong Password", "Error")
		else:
			messagebox.showerror("User not found.", "Error")


	label1=Label(root2, text="Please enter the details below.")
	label1.pack()
	label2=Label(root2, text="")
	label2.pack()

	username_verify=StringVar()
	password_verify=StringVar()
	
	label3=Label(root2, text="Username *")
	label3.pack()
	username_entry1=Entry(root2, textvariable=username_verify)
	username_entry1.pack()

	label3=Label(root2, text="Password *")
	label3.pack()
	password_entry1=Entry(root2, textvariable=password_verify)
	password_entry1.pack()

	label2=Label(root2, text="")
	label2.pack()

	Button(root2, text="Login", width="10", height="2", command=login_verify).pack()


	root2.mainloop()



root.title("Form creating and linking with database.")
root.geometry("500x500")

label1=Label(root, text="Notes 1.0", width="500", height="3", bg="grey")
label1.pack()
label_blank=Label(root, text="").pack()

button_login=Button(root, text="Login", width="30", height="2", command=login_function)
button_login.pack()
label_blank=Label(root, text="").pack()

button_register=Button(root, text="Register", width="30", height="2", command=register)
button_register.pack()

root.mainloop()
