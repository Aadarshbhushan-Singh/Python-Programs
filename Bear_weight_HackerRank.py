weights=list(map(int, input().split()[:2]))
a=weights[0]
b=weights[1]
year=0
while a<=b:
		year+=1
		a*=3
		b*=2
print(year)
