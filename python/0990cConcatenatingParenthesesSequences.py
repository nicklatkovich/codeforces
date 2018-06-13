import math

def parseS(s):
	left = 0
	r = 0
	for k in s:
		r += 1 if k == '(' else -1
		if r < left: left = r
	right = 0
	r = 0
	for k in reversed(s):
		r += 1 if k == ')' else -1
		if r < right: right = r
	if left < 0 and right < 0: return ''
	if left != 0: return left
	return -right


n = int(input())
s = []
for _ in range(n): s.append(list(input()))
a = [x for x in [parseS(seq) for seq in s] if x != '']
c = {}
for i, k in enumerate(a):
	if k not in c: c[k] = 0
	c[k] += 1
result = 0
for k in c:
	count = c[k]
	if k == 0: result += 1 if count == 1 else count * (count - 1) + count
	elif k > 0 and -k in c: result += count * c[-k]
print(int(result))
