starting=int(input("Enter the starting number of the series: "))
len_series=int(input("Enter the length of the series: "))
list_1=[]
for i in range(1,len_series):
	if len(list_1)<2:
		list_1.append(starting)
	if len(list_1)>1:
		a=list_1[len(list_1)-1]+list_1[len(list_1)-2]
		list_1.append(a)
print(list_1)