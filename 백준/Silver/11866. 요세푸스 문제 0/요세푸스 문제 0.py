def main():
    N, K = map(int, input().split())
    people = list(range(1, N + 1))
    target = 0
    res: list[int] = []
    while people:
        target = (target + K - 1) % len(people)
        res.append(people.pop(target))
    print('<', end='')
    print(*res, sep=', ', end='')
    print('>')


if __name__ == '__main__':
    main()
