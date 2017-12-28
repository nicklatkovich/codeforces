sevens = [7 * i for i in range(3)]
for i in range(int(input())):
    num = int(input())
    print('YES' if 0 in [max(-1, num - seven) % 3 for seven in sevens] else 'NO')
