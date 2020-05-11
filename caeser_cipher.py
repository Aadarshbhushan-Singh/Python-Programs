word=input("Enter the word: ").lower()
number=int(input("Enter the number: "))
list_1=[]
list_2=[]
for i in word:
	list_1.append(ord(i))
print ("Order of the word: ",list_1)
for i in list_1:
	sum=i+number
	if sum>122:
		sum=sum-26
	list_2.append(sum)
print ("Order of the code word: ",list_2)
print ("Code word: ",end='')
for i in list_2:
	print (chr(i),end='')
