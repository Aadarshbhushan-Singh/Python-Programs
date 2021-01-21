'''import re
message=('this is a phone number 111-222-333, 333-888-0098 but this is not 888-098-7865')
phonenumber=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
matched=phonenumber.search(message) #search return only one phone number and  we have to print it by adding .group()
print(matched.group())

print(phonenumber.findall(message))  #findall returns a list of the phonenumber or the assigned pattern so we have to print this directly'''


#--------------------- If you want to get only specific numbers from the phone number then use parenthesis.---------------#
import re
message=("This is phone number 444-456-1233")
PhoneNumber=re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
matched=PhoneNumber.search(message)
print(matched.group(1)) #prints the object under first parenthesis
print(matched.group(2)) #prints the objects under second parenthesis


batRegex = re.compile(r'bat(man|mobile|hero|crow)')
matched_bat=batRegex.search("batman is the bathero")
print(matched_bat.group())