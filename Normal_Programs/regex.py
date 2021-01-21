#  Meta Characters
#  [] A set of characters
#  \ Signals a special sequence (can also be used to escape special characters)
#  . Any character (except newline character)
#  ^ Starts with
#  $ Ends with
#  * Zero or more occurrences
#  + One or more occurrences
#  {} Exactly the specified number of occurrences
#  | Either or
#  () Capture and group
#  Special Sequences
#  \A Returns a match if the specified characters are at the beginning of the string
#  \b Returns a match where the specified characters are at the beginning or at the end of a word r"ain\b"
#  \B Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# 
#  \d Returns a match where the string contains digits (numbers from 0-9)
#  \D Returns a match where the string DOES NOT contain digits
#  \s Returns a match where the string contains a white space character
#  \S Returns a match where the string DOES NOT contain a white space character
#  \w Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
#  \W Returns a match where the string DOES NOT contain any word characters
#  \Z Returns a match if the specified characters are at the end of the string  


import re
mystring= '''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
harry bhai lekin
bahut hi badia aadmi aiai 22-44 haiaiinaiiiiiiiiiiii'''


pattern=re.compile(r'fass')
matches=pattern.finditer(mystring)
for i in matches:
	print(i)
pattern1=re.compile(r'North')
matches2=pattern1.finditer(mystring)
for i in matches2:
	print(i)
pattern3=re.compile(r'.com') #Any character after which com is present
matches3=pattern3.finditer(mystring)
for i in matches3:
	print(i)
pattern4=re.compile(r'.')  #Search any characters
matches4=pattern4.finditer(mystring)
# you can print using for loop (Note: Not printed in this because to print all the characters more time is required)

pattern5=re.compile(r'^Tata') #when mystring starts with Tata
matches5=pattern5.finditer(mystring)
for i in matches5:
	print(i)
pattern6=re.compile(r'iii$')
matches6=pattern6.finditer(mystring)
for i in matches6:
	print(i)

pattern7=re.compile(r'ai*') # a and any number of i
matches7=pattern7.finditer(mystring)

pattern8=re.compile(r'ai+')
matches8=pattern8.finditer(mystring)
for i in matches8:
	print(i)

pattern9=re.compile(r'ai{12}') #12 i after a
matches9=pattern9.finditer(mystring)
for i in matches9:
	print(i)

pattern10=re.compile(r'(ai){2}') #matches 2 ai parenthesis forms the group of characters
matches10=pattern10.finditer(mystring)
for i in matches10:
	print(i)

pattern11=re.compile(r'(ai){2}|t') #either (ai) or (t)
matches11=pattern11.finditer(mystring)
for i in matches11:
	print(i)

pattern12=re.compile(r'\d{2}-\d{2}') #2 digits then one dash(-) and again 2 digit
matches12=pattern12.finditer(mystring)
for i in matches12:
	print(i)