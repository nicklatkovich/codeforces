
n = int(input())
result = 0
passengersCount = 0
for i in range(n):
    ai, bi = map(int, input().split())
    passengersCount -= ai
    passengersCount += bi
    result = max(result, passengersCount)
print(result)
