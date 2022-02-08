n=int(input())
for i in range(1,n+1):
    word=input().lower()
    def pelindrome(word):
        reverse_word=word[::-1]
        if reverse_word==word:
            return(True)
        else:
            return(False)
    def symmetry(word):
        first_half=word[0:int((len(word)/2))]
        if len(word)%2==0:
            second_half=word[int((len(word)/2)):len(word)]
        else:
            second_half=word[int((len(word)/2))+1:len(word)]
        if first_half==second_half:
            return(True)
        else:
            return(False)
    if pelindrome(word) is True and symmetry(word) is True:
        print ("Both property")
    elif pelindrome(word) is True and symmetry(word) is False:
        print ("Palindrome")
    elif pelindrome(word) is False and symmetry(word) is True:
        print ("Symmetry")
    else:
        print ("No property")