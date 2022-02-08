def swap_case(s):
    mylist=[]
    for i in s:
        if i.isupper() is True:
            mylist.append(i.lower())
        elif i.islower() is True:
            mylist.append(i.upper())
        else:
            mylist.append(i)
    mystring=''.join(mylist)
    return (mystring)
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)