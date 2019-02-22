n = int(input())
a = [int(x) for x in input().split(' ')]
up, down = [[None for _ in range(n)] for _ in range(2)]
k = lambda list, i: list[i] if i >= 0 and i < n else 0

for i, ai in enumerate(a):
    up[i] = ai + k(up, i - 2)

for i, ai in reversed(list(enumerate(a))):
    down[i] = ai + k(down, i + 2)

result = 0

for i in range(n):
    states = [k(up, i - x) + k(down, i + j + 1) for j, x in enumerate([2, 1])]
    if states[0] == states[1]:
        result += 1

print(result)
