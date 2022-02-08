from itertools import permutations
string=list(map(str,input().split()))
list_01=list(permutations(string[0],int(string[1])))
for i in sorted(list_01):
	for j in i:
		print(j.upper(),end="")
	print()