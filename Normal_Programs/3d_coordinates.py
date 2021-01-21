a=int(input())
b=int(input())
c=int(input())
total=int(input())
x=0
y=0
z=0
sum1=0
coordinates=[]
for x in range(a):
	for y in range(b):
		for z in range(c):
			coordinates.append([x,y,z])
print("without removing: ",coordinates)
for i in coordinates:
	if sum(i)==total:
		coordinates.remove(i)
print("after removing: ",coordinates)

