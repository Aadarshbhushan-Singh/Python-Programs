num=int(input("Enter the number of row: "))
for i in range(0,num):
	for j in range(0,i):
		print(" ",end="")
	for j in range(0,num-i-1):
		print("*",end=" ")
	print()