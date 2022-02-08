def binary_search(list1,key):
    low=0
    high=len(list1)-1
    found=False
    while low<=high and not found:
        mid=(low+high)//2
        if key==list1[mid]:
            found=True
        elif key>list1[mid]:
            low=mid+1
        else:
            high=mid-1
    if found ==True:
        print ("keyword is found")
    else:
        print ("keyword is not found")
        
        



list1=[1,2,45,23,65,21,56]
list1.sort()
print (list1)
key=int(input("Enter the key: "))
binary_search(list1,key)
