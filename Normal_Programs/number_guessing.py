import random
name=input("Enter your name: ").capitalize()
print ("Welcome",name)
list_1=[]
def random_function():
	global list_1
	user_input=input("Enter the number: ")
	computer=random.randint(1,9)
	list_1.append(computer)
	if user_input=='exit':
		print ("Total inputs: ",len(list_1))
		a=input("Enter any character to quit: ")
		quit()
	print ("Computer: ",computer)
	user=int(user_input)
	if (computer-user)<0 and (computer-user)>(-3):
		print ("Less high")
	elif (computer-user)>0 and (computer-user<3):
		print ("less low")
	elif (computer-user)<0 and (computer-user>(-9)):
		print ("Too high")
	elif (computer-user)>0 and (computer-user<9):
		print ("Too low")
	elif (computer-user)==0:
		print ("Exact number")
	random_function()
random_function()