print("Enter the number: ")
n=int(input())
list1=[]
for i in range(n):
    pages_to_read=int(input())
    days=1
    pages_read=1
    sum_pages=1
    product=1
    while sum_pages<=pages_to_read:
        sum_pages=sum_pages+(product*2)
        product*=2
        days+=1
    list1.append(days) 	
for i in list1:
    print(i)