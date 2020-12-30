import os
print(os.getcwd()) #This shows cwd(current working directory)
#os.rename("first.txt","second.txt")  #In the same directory, a file first.txt was present which was changed to second.txt
print(os.listdir()) #os.listdir() returns all the files name present in the directory
os.chdir("C://Users") #This changed my working directory to users in C
print(os.getcwd())
os.chdir("c://Users/Aadarsh Singh/Desktop/Python Programs/Normal Programs")
print(os.getcwd())
f=open("second.txt") #This will open the file within the python shell (RAM)
print("The files present in C drive are: \n")
print(os.listdir("c://")) #This returns list.
os.mkdir("Folder made by python")