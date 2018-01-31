x,[h,m],r=int(input()),list(map(int,input().split(' '))),0
while'7'not in''.join(str(c)for c in[h,m]):
	m,r=m-x,r+1
	if m<0:m,h=m+60,(h+23)%24
print(r)