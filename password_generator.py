import random
import string
letters1=string.ascii_lowercase
letters2=string.ascii_uppercase
symbols=string.punctuation
def strong():
	list1=[]
	list1.append(random.choice(letters1))
	list1.append(random.choice(letters2))
	list1.append(random.choice(symbols))
	list1.append(random.randint(0,10))
	for i in range(1,5):
		list1.append(random.choice(letters1))
	for i in list1:
		print(i,end='')
	print("\n")
	nextcall()

def weak():
	list1=[]
	list1.append(random.randint(0,10))
	for i in range(1,5):
		list1.append(random.choice(letters1))
	for i in list1:
		print(i,end='')
	print("\n")
	nextcall()
def call():
	print("\n")
	level=input("Type weak or strong: ").lower()
	if level=='weak':
		weak()
	elif level=='strong':
		strong()
	else:
		print("Invalid Input")
		call()
def nextcall():
	entry=input("Type next or quit: ")
	if entry=='next':
		call()
	elif entry=='quit':
		quit()
	else:
		print("Invalid Input")
		nextcall()
name=input("Enter your name please: ").upper()
print("HELLO",name,", This is a password generator.\n")
call()