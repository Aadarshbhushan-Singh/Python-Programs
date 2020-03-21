string=input("Enter the string: ")
n=abs(int(input("Enter the number: ")))
if (len(string))>=2:
    print (n*(string[0]+string[1]))
else:
    print (n*string[0])
