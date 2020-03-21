n=int(input())
l=0
m=0
for i in range(1,n+1):
    print ("Enter the value of litre",i,":",end='')
    a=int(input())
    l=l+a
    print ("Enter the value of mililitre",i,":",end='')
    b=int(input())
    m=m+b
if m>1000:
   l=l+( m//1000)
print (l)
print (m%1000)
