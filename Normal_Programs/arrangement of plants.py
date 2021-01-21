n=int(input())
dict_1={}
for i in range(1,n+1):
	plant_id=int(input())
	plant_ht=int(input())
	dict_1.setdefault(plant_id,plant_ht)
sorted_dict_1 = sorted(dict_1.items(), key=lambda x: x[1])
for i in sorted_dict_1:
		print (i[0])