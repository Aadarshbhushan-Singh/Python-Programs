n=int(input())
marksheet=[]
scorelist=[]
for i in range(n):
	name=input()
	score=float(input())
	marksheet+=[[name,score]]
	scorelist+=[score]
scorelist=list(dict.fromkeys(scorelist))
b=sorted(scorelist)[1]
for i in marksheet:
	if i[1]==b:
		print(a)


if __name__ == '__main__':
    marksheet=[]
    scorelist=[]

    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet+=[[name,score]]
        scorelist+=[score]


    scorelist = list(dict.fromkeys(scorelist))
    b=sorted(scorelist)[1] 

    for a,c in sorted(marksheet):
        if c==b:
            print(a)