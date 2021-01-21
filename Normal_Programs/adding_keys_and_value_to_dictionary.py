list_1=[1,2,3,4,5,6,7,8]
list_2=[10,20,30,40,50,60,70,80]
# To merge two list to make a single dictionary
dict_1=dict(zip(list_1, list_2))
print (dict_1)

#if the key is present then the value is not added else the key and value both is added 
dict_1.setdefault(9,90)
print (dict_1)
dict_1.setdefault(9,100)

#adding one by one keys and vlaue to the dictionary
dict_1[10]=100
print (dict_1)

#updaing method to add keys and vlaues or adding multiple keys and value at same time
dict_1.update({11:110, 12:120})
print (dict_1)

dict_2={13:130, 14:150}
dict_1.update(dict_2)
print (dict_1)

#updating the value of a key in dictionary
dict_1[14]=140
print (dict_1)

#printting the values in dictionary
for i in dict_1:
	print (dict_1[i])

#printing the keys in dictionary
for i in dict_1:
	print (i)

#printing keys and vlaue at the same time
for i in dict_1:
	print (i, dict_1[i])

#upadate more than one dictionary////    Merging two or more dictionary
dict_3={16:160, 17:170, 18:180}
dict_4={19:190, 20:200, 21:210}
dict_1={**dict_1,**dict_3, **dict_4}
print (dict_1)

for d in (dict_3, dict_4):
	dict_1.update(d)
print (dict_1)


#printing dictionary keys and values
print (dict_1.keys())
print (dict_1.values())