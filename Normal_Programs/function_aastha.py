def accending(list1):
    for i in range(0,len(list1)):
        for j in range(len(list1)+1,len(list1)):
                       if(list1[i]>list1[j]):
                          temp=list1[i]
                          list1[i]=list1[j]
                          list1[j]=temp
    return list1
                          
                          
list1=[1,9,6,2,8]
print(accending(list1))

list1.sort()
print(list1)

