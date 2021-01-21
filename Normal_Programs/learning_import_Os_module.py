import os
print(os.getcwd()) #This shows cwd(current working directory)
#os.rename("first.txt","second.txt")  #In the same directory, a file first.txt was present which was changed to second.txt
print(os.listdir()) #os.listdir() returns all the files name present in the directory
os.chdir("C://Users") #This changed my working directory to users in C
print(os.getcwd())
os.chdir("c://Users/Aadarsh Singh/Desktop/Python Programs/Normal Programs/learning Os module")
print(os.getcwd())
f=open("second.txt") #This will open the file within the python shell (RAM)
print("The files present in C drive are: \n")
print(os.listdir("c://")) #This returns list.
# os.mkdir("Folder made by python") This can make folder. mkdir(make directory)
# os.rename("learning_import_module.py","learning_import_os_module.py")
#os.makedirs("First level folder/second level folder/ third level folder")
a=os.path.join("c:/", "user")  #This joins the directory and avoid mistakes of slash(/)
print(a)
print(os.path.exists("c://"))
print(os.path.exists("c://Usersssss"))