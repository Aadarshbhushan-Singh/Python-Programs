n=input()
list1=[]
a=list(n)
digit=int(n)
for i in a:
    if int(i)==0:
        continue
    elif digit%(int(i))==0:
        list1.append(i)
if len(list1)==0:
    print ("No factors")
list1.reverse()
if len(list1)==1:
    print(list1[0])
else:
    list2=[]
    for i in list1:
        list2.append(int(i))
    print (str(list2)[1:-1])
