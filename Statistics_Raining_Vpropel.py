num=input()
list1=[]
for i in range(int(num)):
	date,rain=input().split()
	list1.append([date,rain])
jan, feb, march, april, may, june, july, august, september, october, november, december =([] for i in range(12))
for j in list1:
	a=j[0][3:5]
	if int(a)==1:
		jan.append(int(j[1]))
	elif int(a)==2:
		feb.append(int(j[1]))
	elif int(a)==3:
		march.append(int(j[1]))
	elif int(a)==4:
		april.append(int(j[1]))
	elif int(a)==5:
		may.append(int(j[1]))
	elif int(a)==6:
		june.append(int(j[1]))
	elif int(a)==7:
		july.append(int(j[1]))
	elif int(a)==8:
		august.append(int(j[1]))
	elif int(a)==9:
		september.append(int(j[1]))
	elif int(a)==10:
		october.append(int(j[1]))
	elif int(a)==11:
		november.append(int(j[1]))
	elif int(a)==12:
		december.append(int(j[1]))
if len(jan)>0:
	print("Jan", sum(jan)/len(jan))
if len(feb)>0:
	print("Feb",sum(feb)/len(feb))
if len(march)>0:
	print("March", sum(jan)/len(jan))
if len(april)>0:
	print("April",sum(april)/len(april))
if len(may)>0:
	print("May", sum(may)/len(may))
if len(june)>0:
	print("June",sum(june)/len(june))
if len(july)>0:
	print("July", sum(july)/len(july))
if len(august)>0:
	print("August",sum(august)/len(august))
if len(september)>0:
	print("September", sum(september)/len(september))
if len(october)>0:
	print("October",sum(october)/len(october))
if len(november)>0:
	print("Nov", sum(november)/len(november))
if len(december)>0:
	print("Dec",sum(december)/len(december))
