import random
comp=[]
for i in range(0,4):
	comp.append(random.randint(0,9))
print(comp)
guess=1
def CowBull():
	global guess
	print("Guess: ",guess)
	cow=0
	bull=0
	user_input=input()
	user=[]
	for i in user_input:
		user.append(int(i))
	print(user)
	for i in user:
		if int(i) in comp:
			bull+=1
	for i in range(0,4):
			if str(user[i])==str(comp[i]):
				bull-=1
				cow+=1
	print("Cow: ",cow)
	print("Bull: ",bull)
	print()
	if comp==user:
		print("Congrats! You won in",guess,"guesses.")
	else:
		guess+=1
		CowBull()

CowBull()
	