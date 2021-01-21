def check_list(a):
	if a[0]==a[len(a)-1]:
		return True
	else:
		return False
list1=[10,20,30,40,50]
list2=[10,20,30,40,50,10]
print(check_list(list1))
print(check_list(list2))


