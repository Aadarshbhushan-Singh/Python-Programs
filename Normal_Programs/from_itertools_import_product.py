a,b,list1 =[1,2,3], [4,5,6],[]
for i in a:
	for j in b:
		list1.append([i,j])
for i in list1:
	print(tuple(i),end=" ")
print("\nItertools")
from itertools import product
c=[6,7]
print(list(product(c,repeat=2))) # repeat means duplicate c two times and find cartesian product
print(list(product(c,repeat=3)))
D=[[1,92,3],[4,5],[7,8]]
print(*list(product(*D))) #using * before list unpacks the list and returns the tuple type set
