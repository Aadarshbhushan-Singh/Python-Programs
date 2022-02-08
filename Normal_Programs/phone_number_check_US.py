def isPhoneNumber(number):
	if len(number)!=12:
		return False
	for i in range(0,3):
		if number[i].isdigit() is False:
			return False
	if number[3]!='-':
		return False
	for i in range(4,7):
		if number[i].isdigit() is False:
			return False
	if number[7]!='-':
		return False
	for i in range(8,12):
		if number[i].isdigit() is False:
			return False
	return True

message=('hello this is phone number 470-333-000 and this is also a phone number 333-456-097 but this it not 44-098-0980')
foundnumber=False
for i in range(len(message)):
	chunk=message[i:i+12]
	if isPhoneNumber(chunk) is True:
		print(chunk)
		foundnumber=True
if foundnumber is False:
	print("No number found")

	