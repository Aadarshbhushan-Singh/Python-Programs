list1=[]
n=int(input("Enter the number you want to enter: "))
for i in range(n):
      number=int(input())
      list1.append(number)
for elements in list1:
    print ('#'*elements)
