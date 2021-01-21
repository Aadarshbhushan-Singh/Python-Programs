def isPhoneNumber(number):
	def firsttwo(number):  #check the two digit
		if len(number)!=10: #check the length of phone number
			for i in range(0,10):
				if number[i].isdigit() is False: #check if all are digits
					return False
			if number[0]!=9: #first number should be 9
				if number[1]!=8: #second number should be 8
					return False
		return True
	if firsttwo(number) is True:
		if number[2]=='1' or number[2]=='0': #chekc for ncell or ntc
			print("NCell")
		elif number[2]=='4' or number[2]=='5' or number[2]=='6': #check for ncell or ntc
			print("Ntc")
		else:
			print("Wrong Phone number")
	else:
		print("Invalid")
	firsttwo(number) #calling the function

isPhoneNumber('9804035362')
isPhoneNumber('9816306875')
isPhoneNumber('9842428507')
isPhoneNumber('9852067543')
isPhoneNumber('98765543321')
isPhoneNumber('d7861432434')
isPhoneNumber('1234567890')
