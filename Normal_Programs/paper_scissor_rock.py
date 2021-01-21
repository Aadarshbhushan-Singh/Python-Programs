import random

def main_function():
	global player
	list1=['paper','scissor','rock']
	computer=random.choice(list1)
	print ("Computer :",computer)
	if (player=='scissor' and computer=='paper') or (player=='rock' and computer=='scissor') or(player=='paper' and computer=='rock'):
		print ("Congratlations. You won!")
	elif player==computer:
		print ("Tie match")
	else:
		print ("Try next time.")
	again=input("Type again to play and any other buttons to end the game: ").lower()
	if again=='again':
		again_function()
	else:
		quit()

def again_function():
	print (name,":",end='')
	player=input().lower()
	if player!='paper' and player!='scissor' and player!='rock':
		print ("You have done typing mistake. Please choose between paper, scissor and rock.")
		player_function()
	else:
		main_function()


def player_function():
	global player
	print (name,":",end='')
	player=input().lower()
	if player!='paper' and player!='scissor' and player!='rock':
		print ("You have done typing mistake. Please choose between paper, scissor and rock.")
		player_function()
	else:
		main_function()

name=input("Enter your name: ").capitalize()
print ("Welcome",name)
print ("This is paper-scissor-rock game. Please choose your option.")
player_function()