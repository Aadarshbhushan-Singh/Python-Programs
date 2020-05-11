string=input()
sub_string=input()
k=0
for i in range(0,len(string)):
	if string[i:i+len(sub_string)]==sub_string:
		k+=1
print(k)