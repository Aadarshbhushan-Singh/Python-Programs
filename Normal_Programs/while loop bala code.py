n=int(input("Enter the number of students: "))
i=1
sum=0
while i<=n:
    print("Enter the marks of student",i)
    marks=int(input("Enter marks"))
    sum=sum+marks
    i=i+1
    average=sum/n
print(average)
