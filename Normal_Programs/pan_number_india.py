def isPanNumber(number):
	if len(number)!=10:
		return False #Length is less or greater
	for i in range(0,5):
		if number[i].isalpha() is False:
			return False
	for i in range(5,9):
		if number[i].isdigit() is False:
			return False
	if number[9].isalpha() is False:
		return False
	return True

print(isPanNumber('abcde1234f'))
print(isPanNumber('123asdf45'))
print(isPanNumber('jasdf???g'))
print(isPanNumber('AABCI6363G'))
