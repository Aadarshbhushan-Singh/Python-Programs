This program can make 100 folders at once
import os
a=os.getcwd()
i=1
while i<101:
	os.makedirs("folder"+str(i))
	i=i+1

