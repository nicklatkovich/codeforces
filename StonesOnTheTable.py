# 266A

n = input()
s = input()
prevC = None
result = 0
for c in s:
    if c == prevC:
        result += 1
    prevC = c
print(result)
