num1=int(input("Enter the number: "))
num2=int(input("Enter the second number: "))
set1=[]
set2=[]
set3=[]
for i in range(1,num1+1):
    if (num1%i)==0:
        set1.append(i)
print (set1)
for i in range(1,num2+1):
    if (num2%i)==0:
        set2.append(i)
print (set2)
for i in set1:
    if i in set2:
        set3.append(i)
print (set3)
for i in set3:
    if i in set3:
        set3.append(i)
    a=max(set3)
    break
print (a)
