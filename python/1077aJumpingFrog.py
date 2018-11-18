t=int(input())
for i in range(t):
	a,b,k=[int(n)for n in input().split()]
	double_step=a-b
	print(k//2*double_step if k%2==0 else k//2*double_step+a)
