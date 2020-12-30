amount=int(input())
one=0
two=0
five=0
ten=0
twenty=0
fifty=0
hundred=0
fivehundred=0
thousand=0
def NumberNotes(amount):
	global one
	global two
	global five
	global ten
	global twenty
	global fifty
	global hundred
	global fivehundred
	global thousand

	if amount>=1000:
		a=amount//1000
		thousand=thousand+a
		amount=amount%1000
		NumberNotes(amount)
	elif amount>=500:
		a=amount//500
		fivehundred=fivehundred+a
		amount=amount%500
		NumberNotes(amount)
	elif amount>=100:
		a=amount//100
		hundred=hundred+a
		amount=amount%100
		NumberNotes(amount)
	elif amount>=50:
		a=amount//50
		fifty=fifty+a
		amount=amount%50
		NumberNotes(amount)
	elif amount>=20:
		a=amount//20
		twenty=twenty+a
		amount=amount%20
		NumberNotes(amount)
	elif amount>=10:
		a=amount//10
		ten=ten+a
		amount=amount%10
		NumberNotes(amount)
	elif amount>=5:
		a=amount//5
		five=five+a
		amount=amount%5
		NumberNotes(amount)
	elif amount>=2:
		a=amount//2
		two=two+a
		amount=amount%2
		NumberNotes(amount)
	elif amount>=1:
		a=amount//1
		one=one+a
		amount=amount%1
		NumberNotes(amount)
NumberNotes(amount)
print("One: ",one)
print("Two: ",two)
print("Five: ",five)
print("Ten: ",ten)
print("Twenty: ",twenty)
print("Fifty: ",fifty)
print("Hundred: ",hundred)
print("Five Hundred: ",fivehundred)
print("Thousands: ",thousand)
