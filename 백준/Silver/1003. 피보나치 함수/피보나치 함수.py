def main():
    T = int(input())
    res = [(1, 0), (0, 1)]
    for _ in range(T):
        N = int(input())
        while len(res) < N + 1:
            count = tuple(map(sum, zip(res[-1], res[-2])))
            res.append(count)
        print(*res[N])


if __name__ == '__main__':
    main()
