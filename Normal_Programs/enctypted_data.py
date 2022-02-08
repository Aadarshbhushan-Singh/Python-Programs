n=int(input("Enter the number: "))
list1=[]
for i in range(0,n):
    ele=input()
    if (ele.isdigit() is False):
        exit()
    else:
        list1.append(int(ele))
        
sum=sum(list1)
sum_str=str(sum)
factor=0
for i in sum_str:
    factor=factor+int(i)
print(factor)
for i in range(0, len(list1)):
    list1[i]=list1[i]+factor;
list1.append(sum)
print(list1)
