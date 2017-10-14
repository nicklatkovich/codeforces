# 873A


class Work:
    def __init__(self, usedTime: int, _id: int):
        self.usedTime = usedTime
        self.id = _id

    def __lt__(self, other):
        if type(other) != Work:
            return
        return self.usedTime < other.usedTime


def main() -> None:
    n, k, x = map(int, str(input()).split())
    _3longestWorks = []
    a = list(map(int, str(input()).split()))
    for i in range(n):
        if len(_3longestWorks) < k or _3longestWorks[0].usedTime < a[i]:
            _3longestWorks.append(Work(a[i], i))
            _3longestWorks.sort()
            if len(_3longestWorks) > k:
                del _3longestWorks[0]
    for longestWork in _3longestWorks:
        a[longestWork.id] = x
    result = 0
    for time in a:
        result += time
    print(result)


main()
