import random
name=input("Enter your name: ").capitalize()
print("Hello",name,"This is world guessing game. Guess the number from 1 to 9")
computer=[]
for i in range(1,5):
	computer.append(random.randint(1,9))
print(computer)
print("Guess your number: ")
def user_function():
	global user
	user=[]
	for i in range(1,5):
		n=input()
		if n.isdigit() is True and len(n)==1:
			user.append(n)
		else:
			print("Invalid Input")
			print("This is new input")
			user_function()
	print(user)
	correct_numbers_function()
def correct_numbers_function():
	global user
	global computer
	correct_numbers=0
	for i in user:
		if int(i) in computer:
			correct_numbers+=1
	print("Correct numbers=: ",correct_numbers)
	print("Wrong numbers: ",(4-correct_numbers))

def correct_place_function():
	global user
	global computer
	correct_place=0
	for i in user:
		if user[int(i)]==
	print("Correct numbers=: ",correct_numbers)
	
correct_place_function()
user_function()