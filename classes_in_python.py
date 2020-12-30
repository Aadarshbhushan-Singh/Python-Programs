class Robot:  #Initializing class. 'Robot' is the name of the class.
	def self_introduction(self):   #self is the argument passed which will be stored by the function.
		print("My name is "+self.name)   #self.name means the object will be stored in variable self which will be assigned by another varibale
		print("I am ",self.age,"years old.")
		print()
r1=Robot()   #r1 is the name of the variable assigned to class Robot
r1.name="tom"
r1.age=45

r2=Robot()  #r2 is the name of the variable assigned to class Robot
r2.name="Harry"
r2.age=67

r1.self_introduction()  #calling the function in the class but argument passed in initial.
r2.self_introduction()


#defining class using def __init__():

class Rectangle:
	def __init__(rect, length, breadth, height):
		rect.length=length
		rect.breadth=breadth
		rect.height=height
	def print_parameters(rect):
		print("Length: ",rect.length)
		print("Breadth: ",rect.breadth)
		print("Height: ",rect.height)
		print()
		
p1=Rectangle(21,32,43)
p2=Rectangle(12,23,34)

p1.print_parameters()
p2.print_parameters()