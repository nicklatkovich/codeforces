q = int(input())
for _ in range(q):
    n, a, b = [int(x) for x in input().split(' ')]
    print(n * a if b > 2 * a else n // 2 * b + a * (n % 2))
