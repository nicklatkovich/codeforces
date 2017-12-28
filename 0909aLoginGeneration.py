[a,b],r=input().split(),''
for i,c in enumerate(a):
	if i==0 or c<b[0]:r+=c
	else:break
print(r+b[0])