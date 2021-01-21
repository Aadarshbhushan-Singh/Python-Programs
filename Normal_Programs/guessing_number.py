###################-----------------------------METHOD NO 1--------------------------######################
import random
name=input("Enter your manhoos name please: ")
print("Hello",name,"Well, I am thinking of a number between 1 and 20 inclusive.")
comp_num=random.randint(1,20)
print("Comp: ",comp_num)

def guess_function():
	global comp_num
	user=int(input("Take your guess: "))
	if user>20 or user<1:
		print("Wrong Input. Common man, you have to guess the number between 1 and 20 inclusive.")
		guess_function()
	else:
		if (comp_num-user)>0:
			print("Your number is low.")
			guess_function()
		elif (comp_num-user)<0:
			print("Your number is high.")
			guess_function()
		elif (comp_num==user):
			print("Great you have choosed the correct number. Now go out and dance.")
			next_game()
			
def next_game():
	next_game_input=input("Enter again to play another game and exit to quit.")
	if next_game_input=='again':
		guess_function()
	elif next_game_input=='exit':
		quit()
	else:
		print("You stupid! You have given wrong input.")
		next_game()

guess_function()

###################-----------------------------METHOD NO 2--------------------------######################
'''import random
name=input("Enter your manhoos name please: ")
print("Hello",name,"Well, I am thinking of a number between 1 and 20 inclusive.")
comp_num=random.randint(1,20)
def guess_number():
	global comp_num
	global user
	global i
	for i in range(1,7):
		user=int(input("Take your geuss."))
		if comp_num-user>0:
			print("Low")
		elif comp_num-user<0:
			print("High")
		else:
			break;
	check_number()
def check_number():
	global comp_name
	global user
	if comp_num==user:
		print("Congrats You have guessed correct number in %d times."%i)
		another_game=input("again or quit")
		if another_game=='again':
			guess_number()
		else:
			quit()
	else:
		print("You were unsucessful to guess.")
		another_game=input("Again to play again and anothe button to quit.")
		if another_game=='again':
			guess_number()
		else:
			quit()

guess_number()'''
