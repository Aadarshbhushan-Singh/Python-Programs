list1=list(map(int, input().split()[:5]))
list2=[]
for i in range(0,5):
	a=list1.count(list1[i])
	if a>1 and a<4:
		list2.append(list1[i]*a)
if len(list2)>=1:
	b=max(list2)
else:
	b=0
print(sum(list1)-b)