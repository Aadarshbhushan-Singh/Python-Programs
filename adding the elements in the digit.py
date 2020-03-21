n=input()
sum=0
a=str(n)
b=list(a)
if n.isdigit()==False:
    print ("Invalid input")
else:
    for i in b:
        sum=sum+int(i)
    print (sum)
