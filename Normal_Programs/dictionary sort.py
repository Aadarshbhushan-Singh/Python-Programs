text='I am aadarsh singh'
dict1={}
for i in text:
	dict1.setdefault(i,0)
	dict1[i]=dict1[i]+1
dict_value=sorted(dict1.items(), key = lambda x: x[1])
print ("Sorted by value: ",dict_value)
dict_key=sorted(dict1.items(), key = lambda x: x[0])
print ("Sorted by key: ",dict_key)


print ("Unsorted",dict1)
inv_dict = {}
for k, v in dict1.items():
    inv_dict.setdefault(v, []).append(k)
print (inv_dict)
