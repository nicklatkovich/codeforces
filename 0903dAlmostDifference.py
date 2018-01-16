n,a,r=int(input()),list(map(int,input().split())),0
print(sum([sum([y-x if abs(x-y)>1 else 0 for y in a[i+1:]])for i,x in enumerate(a[:-1])]))
# TODO: rewrite to the algorithm described in the .md file