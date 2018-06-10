n = list(input())
ends = ['00', '25', '50', '75']
res = -1


def can_be_result(indeces):
	if -1 in indeces: return False
	t = [x for i, x in enumerate(n) if i not in indeces]
	if len(t) == 0: return True
	if len([x for x in t if x != '0']) == 0: return False
	return True
	

for end in ends:
	indeces = [-1 for _ in end]
	for i in reversed(range(len(n))):
		for j in reversed(range(len(end))):
			if indeces[j] == -1 and n[i] == end[j]:
				indeces[j] = i
				break
	if not can_be_result(indeces): continue
	temp = [x for x in n]
	preres = 0
	while len([0 for i, x in enumerate(reversed(end)) if temp[-(i + 1)] == x]) != len(end):
		for i in reversed(range(len(indeces))):
			if indeces[i] != len(n) - len(end) + i:
				left = indeces[i]
				right = left + 1
				if left == 0:
					while temp[right] == '0':
						left += 1
						right += 1
				temp[left], temp[right] = temp[right], temp[left]
				indeces = [x + 1 if x == left else x - 1 if x == right else x for i, x in enumerate(indeces)]
				preres += 1
				break
	if res == -1 or preres < res: res = preres

print(res)
