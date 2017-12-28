import math
def o(x):return x*(x+1)/2
n=int(input())
print(math.round(2*o(math.floor(n/2))+(math.ceil(n/2)if n%2==1 else 0)))