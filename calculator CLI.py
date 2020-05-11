def main_function():

	def addition():
		number=int(input("How many numbers you want to add? "))
		sum=0
		for i in range(1,number+1):
			print ("Enter the num",i,':',end='')
			num=int(input())
			sum=sum+num
		print ("The sum of the numbers is: ",sum)
		again=input("Press cont or quit: ")
		if again=='cont':
			first_function()
		else: 
			quit()


	def difference():
		num1=int(input("Enter the first number: "))
		num2=int(input("Enter the second number: "))
		difference=num1-num2
		print("The differnece of first and second number is: ",difference)
		again=input("Press cont or quit: ")
		if again=='cont':
			first_function()
		else: 
			quit()

		
	def product():
		number=int(input("How many numbers you want to multiply? "))
		product=1
		for i in range(1,number+1):
			print ("Enter the num",i,':',end='')
			num=int(input())
			product=product*num
		print ("The product of the numbers is: ",product)
		again=input("Press cont or quit: ")
		if again=='cont':
			first_function()
		else: 
			quit()

	def division():
		num1=int(input("Enter the first number: "))
		num2=int(input("Enter the second number: "))
		division=num1/num2
		remainder=num1%num2
		dividend=num1//num2
		print ("The dividend is: ",dividend)
		print ("The remainder is: ",remainder)
		print ("The perfect division is: ",division)
		again=input("Press cont or quit: ")
		if again=='cont':
			first_function()
		else: 
			quit()


	global operator
	if operator=='-':
		difference()
	elif operator=='+':
		addition()
	elif operator=='*':
		product()
	elif operator=='/':
		division()



def first_function():
	ope_list=['+','-','*','/']
	global operator
	operator=input("Enter the operator['+','-','*','/']: ")
	if operator not in ope_list:
		print ("Invalid Operator")
		again=input("Press cont or quit: ")
		if again=='cont':
			first_function()
		else:
			quit()
	else:
		main_function()
name=input("Enter your name: ").capitalize()
print ("WELCOME "+name)
print ("This is Command Line Interface Calculator.")
first_function()
	