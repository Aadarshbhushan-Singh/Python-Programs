first_w=input().rstrip()
second_w=input().rstrip()
third_w=input().rstrip()
list_1=list(first_w)
list_2=list(second_w)
list_3=list(third_w)
list_a=[]
list_b=[]
list_c=[]
for i in list_1:
    if i in list_2 and i in list_3:
        list_a.append(i)
list_a.sort()
set_a=list(set(list_a))
for i in list_1:
    if i in list_2 and i not in list_3:
        list_b.append(i)
list_b.sort()
set_b=list(set(list_b))
for i in list_1:
    if i not in list_2 and i not in list_3:
        list_c.append(i)
list_c.sort()
set_c=list(set(list_c))
list_d=set(list_1+list_2+list_3)
list_e=list(list_d)
print (set_a)
print (set_b)
print (set_c)
print (sorted(list_e))