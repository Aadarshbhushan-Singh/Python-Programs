n=input()
list_con=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
sum=1
for i in n:
    if i in list_con:
        sum=sum+1
    else:
        sum=0
if sum!=0:
    print ("Consogram")
else:
    print ("Not consogram")