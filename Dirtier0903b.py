def read():return list(map(int,input().split()))
[[h1,a1,c1],[h2,a2]],b=[read()for i in range(2)],[]
while h2>0:
	if h1>a2 or h2<=a1:
		h2-=a1
		b.append(True)
	else:
		h1+=c1
		b.append(False)
	h1-=a2
print(len(b))
for o in b:print('STRIKE'if o else'HEAL')