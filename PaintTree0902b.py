def o():return list(map(int,input().split()))
[n],[p,c]=o(),[o()for x in range(2)]
print(sum([1 if i==0 or c[p[i-1]-1]!=c[i]else 0 for i in range(n)]))