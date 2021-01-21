'''n=int(input())
listfinal=[]
for i in range(n):
    m=int(input())
    list1=list(map(int, input().split()[:m]))
    listcube=[]
    if len(list1)%2==0:
        for i in range(int((len(list1))/2)):
            if list1[i]>=list1[len(list1)-i-1]:
                listcube.append(list1[i])
            else:
                listcube.append(list1[len(list1)-i-1])
            if list1[i]<list1[len(list1)-i-1]:
                listcube.append(list1[i])
            else:
                listcube.append(list1[len(list1)-i-1])
    else:
        for i in range(int((len(list1))/2)):
            if list1[i]>=list1[len(list1)-i-1]:
                listcube.append(list1[i])
            else:
                listcube.append(list1[len(list1)-i-1])
            if list1[i]<list1[len(list1)-i-1]:
                listcube.append(list1[i])
            else:
                listcube.append(list1[len(list1)-i-1])
        listcube.append(list1[int(len(list1)/2)])

    list2=sorted(list1, reverse=True)
    if listcube==list2:
        listfinal.append('y')
    else:
        listfinal.append('n')
for i in listfinal:
    if i=='y':
        print("Yes")
    elif i=='n':
        print("No")'''

for i in range(int(input())):
	input()
	lst=[int(i) for i in input().split()]
	