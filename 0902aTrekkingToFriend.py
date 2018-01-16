def o():return list(map(int,input().split()))
[n,m],r=o(),{}
for i in range(n):
	[a,b]=o()
	r[a]=max(b,r[a])if a in r else b
w=[True if i==0 else False for i in range(m+1)]
for i,a in enumerate(w):
	if a==False:break
	if i in r:
		for j in range(i,r[i]+1):w[j]=True
print('YES'if w[m]else'NO')