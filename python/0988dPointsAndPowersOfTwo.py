import math

powers = [2 ** i for i in range(0, 31)]

def f(s):
	for k in s:
		for j in powers:
			a = k - j
			b = k + j
			if a in s and b in s: return [a, k, b]
	for k in s:
		for j in powers:
			b = k + j
			if b in s: return [k, b]
	return [next(iter(s))]


def main():
	_ = input()
	x = set(int(x) for x in input().split())
	res = f(x)
	print(len(res))
	print(' '.join(str(x) for x in res))


main()
