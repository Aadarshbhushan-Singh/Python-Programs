n=input()
list1=list(n)
sum_digit=0
sum_char=0
for i in list1:
    if i.isdigit() is True:
        sum_digit+=1
    if i.isdigit() is False and i.isalpha() is False:
        sum_char+=1
if list1[0].isalpha() is False:
    print ("Invalid")
elif len(list1)<8:
    print ("Invalid")
elif sum_digit==0 or sum_char==0:
    print ("Invalid")
else:
    print ("Valid")