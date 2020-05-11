n=int(input())
list_name=[]
list_grade=[]
for i in range(0,n):
	name=input()
	list_name.append(name)
	grade=float(input())
	list_grade.append(grade)
a = min(list_grade)
for i in range(n):
	if a==min(list_grade):
		list_grade.remove(min(list_grade))
b==min(list_grade)
for i in list_grade:
	if b==i:
		c=list_grade.index


