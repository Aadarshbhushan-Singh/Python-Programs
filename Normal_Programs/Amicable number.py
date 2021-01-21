num_one=int(input())
num_two=int(input())
factor_num_one=[]
factor_num_two=[]
for i in range(1,num_one):
    if num_one%i==0:
        factor_num_one.append(i)
    if num_two%i==0:
        factor_num_two.append(i)
if (num_one)<0 or (num_two)<0:
    print ("Invalid Input")
elif sum(factor_num_one)==num_two and sum(factor_num_two)==num_one:
    print ("Yes")
else:
    print ("No")