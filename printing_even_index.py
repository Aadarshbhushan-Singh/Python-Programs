def string_function(string):
	for i in string:
		if string.index(i)%2==0:
			print("index[",string.index(i),"]",i)
a=input("Enter the string: ")
print("Original string is: ",a)
print("String with even indices is.")
string_function(a)
