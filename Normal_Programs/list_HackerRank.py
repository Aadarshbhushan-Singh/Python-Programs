n=int(input())
list1=[]
for i in range(n):
	x=input.split()
	if x[0]=='insert':
		list1.insert(int(x[1]),x[2])
	elif x[0]=='print':
		print(list1)
	elif x[0]=='remove':
		list1.remove(x[1])
	elif x[0]=='append':
		list1.append(x[1])
	elif x[0]=='sort':
		list1.sort()
	elif x[0]=='pop':
		list1.pop(x[1])
	elif x[0]=='reverse':
		list1.reverse()