n=int(input())
list1=[]
list2=[]
for i in range(1,n+1):
    print ("Enter the value of litre",i,":",end='')
    a=int(input())
    list1.append(a)
    print ("Enter the value of mililitre",i,":",end='')
    b=int(input())
    list2.append(b)
a=sum(list1)
b=sum(list2)
if b>1000:
   a=a+( b//1000)
print (a)
print (b%1000)
