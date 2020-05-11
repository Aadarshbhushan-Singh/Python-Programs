n=int(input())
for i in range(0,n):
	sum=0
	if i==0:
		print("Current number ",i,"previous number ",i,"sum",i)
	if i>0:
		print("Current number ",i,"previous number ",i-1,"sum",i+i-1)

