n,s,p,g=int(input()),[1],True,7+10**9
for i in range(n):
	m,l=input()=='s',len(s)
	if not p:s=[0]+s
	else:
		t=[0]*l
		for j in range(l):
			
		s=[sum(s[i:])%g for i in range(len(s))]
	p=m
print(sum(s)%g)
# more productive solution - ../Cpp/IndentationInPython0909c.cpp
