def remove_char(string, num):
	list1=list(string)
	for i in range(0,num):
		list1.remove(list1[0])
	for j in list1:
		print(j,end='')
remove_char('pynative', 4)
