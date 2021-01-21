def minion_game(string):
	string=string.upper()
	staurt, kevin = 0, 0
	list_string=[]
	vowel=['A','E','I','O','U']
	for i in range(len(string)):
		letter=""
		for j in range(i,len(string)):
			letter=letter+string[j]
			list_string.append(letter)
	for i in list_string:
		if i[0] in vowel:
			kevin+=1
		else:
			staurt+=1
	if staurt>kevin:
		print("Stuart",staurt)
	elif kevin>staurt:
		print("Kevin",kevin)
	else:
		print("Draw")
s=input()
minion_game(s)


