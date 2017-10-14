# 873B


def rIndex(l: list, value) -> int:
    return len(l) - l[::-1].index(value) - 1


def main() -> None:
    n = int(input())
    s = str(input())
    cnt0 = []
    cnt0Count = 0
    cnt1 = []
    cnt1Count = 0
    b = []
    for c in s:
        if c == '1':
            cnt1Count += 1
        else:
            cnt0Count += 1
        cnt0.append(cnt0Count)
        cnt1.append(cnt1Count)
        b.append(cnt1Count - cnt0Count)
    usedB = []
    result = 0
    for i in range(n):
        if b[i] in usedB:
            continue
        j = rIndex(b, b[i])
        result = max(result, j - i)
        usedB.append(b[i])
    print(result)


main()
