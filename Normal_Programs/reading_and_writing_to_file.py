'''f=open('text.txt','w')
print(f.name)
print(f.mode)
f.close()

In the above method, the closing of the file is compulory. We will use with method in which the closing of the file is atuomatic.'''
'''with open('text.txt', 'r') as f:
		#for lines in f:
		#	print(lines, end='')

		f_content=f.read(100) #This reads the whole document as it is. The argument passed prints the character. This prints the first 100 characters from the file.
		print(f_content)
		#f_content2=f.readlines()  #This read the elements of the file as list.
		#print(f_content2,end='')
		#f_content3=f.readline()  #This reads the first line of the file in string form. when you write this code again then another line is added.
		#print(f_content3,end='')'''

quantity = 3
totalMoney = 1000
price = 450
print("I have",totalMoney,"dollars so I can buy",quantity,"footbals for",round(price,2),"dollars")
print("I have %d dollars so I can buy %d footbals for %d dollars."%(totalMoney,quantity,price))
