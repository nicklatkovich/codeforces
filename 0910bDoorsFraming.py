import math
[n,a,b],r,i,j=[int(input())for x in range(3)],6,4,5
while i>=0:
	l,c,o=[b if x in[i,j]else a for x in range(6)],0,n
	for k in l:(o,c)=(n-k,c+1)if o<k else(o-k,c)
	r,j=min(r,c if o==n else c+1),j-1
	if i==j:i,j=i-1,5
print(r)