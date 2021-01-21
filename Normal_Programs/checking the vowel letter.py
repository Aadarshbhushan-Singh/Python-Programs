letter=input("Enter the letter: ")
vowel=['a','e','i','o','u']
if len(letter)>1:
    print ("invalid input")
elif letter in vowel:
    print("This is vowel letter.")
else:
    print ("This is not vowel letter.")
