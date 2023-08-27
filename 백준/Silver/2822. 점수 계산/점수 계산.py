import heapq


def main():
    problems = 8
    ls: list[tuple[int, int]] = []
    heapq.heapify(ls)
    for p in range(1, problems + 1):
        score = int(input())
        heapq.heappush(ls, (-score, p))

    ans = 5
    total = 0
    res: list[int] = []
    for _ in range(ans):
        temp = heapq.heappop(ls)
        total += -temp[0]
        res.append(temp[1])

    print(total)
    print(*sorted(res))


if __name__ == '__main__':
    main()
