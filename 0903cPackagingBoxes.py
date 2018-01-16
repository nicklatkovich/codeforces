n,a=input(),list(map(int,input().split()))
print(max({i:a.count(i)for i in a}.values()))