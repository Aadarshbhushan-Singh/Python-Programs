date1=list(map(int, input().split()[:3]))
date2=list(map(int, input().split()[:3]))
if date1[2]-date2[2]==0:
	if date1[1]-date2[1]==0:
		if date1[0]-date2[0]==0:
			fine=0
		else:
			fine=(date1[0]-date2[0])*15
	else:
		fine=(date1[1]-date2[1])*500
else:
	fine=(date1[2]-date2[2])*10000
print(fine)