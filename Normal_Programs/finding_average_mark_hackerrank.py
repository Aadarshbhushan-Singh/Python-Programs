n=int(input("Enter the number: "))
dict1={}
for i in range(n):
	name, score1, score2, score3=input().split()
	dict1.setdefault(name, [int(score1), int(score2), int(score3)])
find_name=input("Enter the name")
total_sum=sum(dict1[find_name])
print("%.2f" % (total_sum/3))

