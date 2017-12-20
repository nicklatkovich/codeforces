n,a=input(),list(map(int,input().split()))
c={i:a.count(i)for i in a}
print(max(c.values()))