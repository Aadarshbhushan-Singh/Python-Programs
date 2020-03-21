a=int(input())

m=[]
sx=0
sy=0

for i in range(a):
    n=[]
    for j in range(a):
        n.append(int(input()))
    m.append(n)
    
for b in range(len(m)):
    sx+=m[b][b]
    sy+=m[b][a-1-b]
    
diff=abs(sx-sy)
print(diff)
