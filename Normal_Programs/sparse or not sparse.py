rows=int(input())
cols=int(input())
def matrix(a,b):
    list1=[]
    list2=[]
    product=a*b
    for i in range(1,product+1):
        n=int(input())
        if n==0:
            list1.append(n)
        else:
            list2.append(n)
    if len(list1)==len(list2) or len(list1)>len(list2):
        print ("Sparse")
    else:
        print ("Not sparse")
if rows!=0 and cols!=0:
    matrix(rows,cols)
else:
    print ("Invalid input")
    
    
