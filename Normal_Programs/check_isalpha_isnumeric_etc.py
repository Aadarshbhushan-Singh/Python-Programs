if __name__ == '__main__':
    s = input()
    a=0
    for i in s:
        if i.isalnum() is True:
            a+=1
    if a==0:
        print("False")
    else:
        print("True")
    b=0
    for i in s:
        if i.isalpha() is True:
            b+=1
    if b==0:
        print("False")
    else:
        print("True")
    c=0
    for i in s:
        if i.isdigit() is True:
            c+=1
    if c==0:
        print("False")
    else:
        print("True")
    d=0
    for i in s:
        if i.islower() is True:
            d+=1
    if d==0:
        print("False")
    else:
        print("True")
    e=0
    for i in s:
        if i.isupper() is True:
            e+=1
    if e==0:
        print("False")
    else:
        print("True")