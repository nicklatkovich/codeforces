[n,d],s,r,i=list(map(int,input().split())),list(map(lambda x:x=='1',list(input()))),0,0
while i!=n-1:
	for j in reversed(range(i,min(i+d+1,n))):
		if j==i:
			print(-1)
			quit()
		if s[j]:
			i=j
			break
	r+=1
print(r)