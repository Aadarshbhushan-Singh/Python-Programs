list_1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
text=input().lower()
sum=1
for i in list_1:
	if i in text:
		sum=sum+1
	else:
		sum=0
if sum==0:
	print ("Not pangram")
else:
	print ("Pangram")
