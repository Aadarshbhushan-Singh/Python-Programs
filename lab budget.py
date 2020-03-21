numberofcomputer=int(input("Enter the number of one computer: "))
rateofcomputer=float(input("Enter the rate of one computer: "))
numberoffurniture=int(input("Enter the number of furniture: "))
rateoffurniture=float(input("Enter the rate of furniture: "))
numberoflabor=int(input("Enter the number of labor: "))
rateoflabor=float(input("Enter the rate of labor: "))
totalbudget=numberofcomputer*rateofcomputer+numberoffurniture*rateoffurniture+numberoflabor*rateoflabor
print("The total budget of the lab is: ",totalbudget)
