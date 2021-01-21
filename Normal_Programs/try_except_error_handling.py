def int_test():
    try:
        num1=int(input())
        print(num1)
        num2=int(input())
        print(num2)
        num3=int(input())
        print(num3)
        num4=int(input())
        print(num4)
    except ValueError:
            print("Error: You have not entered an integer")


def division_function(num):
    try:
        return 100/num
    except:  #If the name of the error is not mentioned then it detects all types of errors.
        print("Detects all error.")
print(division_function(10))
print(division_function(8))
print(division_function(0))
print(division_function(20))
print(division_function(5))

def division_function(num):
    try:
        return 100/num
    except ZeroDivisionError:
        print("Detects ZeroDivisionError.")
print(division_function(10))
print(division_function(8))
print(division_function(0))
print(division_function(20))
print(division_function(5))

int_test()


