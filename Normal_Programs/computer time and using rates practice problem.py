hr=int(input("Enter the number of hours: "))
min=int(input("Enter the number of minutes: "))
amount=200
if hr>7:
    print("You have used it for long time.")
elif min>59:
    print("Invalid Input")
elif hr<5:
    print(amount)
elif hr>5:
    amount=((200+(hr-5)*50)+(min*1))
print(amount)
