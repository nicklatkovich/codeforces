def f(x):
	r=0
	while x:r,x=r+x%10,x//10
	return r
k,r=int(input()),18
while k:
	r+=1
	if f(r)==10:k-=1
print(r)