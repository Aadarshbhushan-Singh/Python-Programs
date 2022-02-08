dict_1={1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
print ("keys in sorted order: ",end='')
for i in sorted(dict_1):
	print (i, end=',')
print ("\nValues in sorted order: ",end='')
for i in sorted(dict_1):
	print (dict_1[i], end=',')

################  For reverse sorted   #######################3333
print ("\nkeys in reverse sorted order: ",end='')
for i in reversed(sorted(dict_1)):
	print (i, end=',')
print ("\nValues reverse in sorted order: ",end='')
for i in reversed(sorted(dict_1)):
	print (dict_1[i], end=',')