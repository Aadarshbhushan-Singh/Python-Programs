n=int(input())
i=1
sum=0
for i in range (1,n):
    if i%2==0:
        sum=sum+i
if sum==n:
    print('perfect number')
elif n<0:
    print('invalid input')
else:
    print ('not a perfect number')
