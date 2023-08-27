def main():
    N = int(input())
    mts = list(map(int, input().split()))
    print(find_kills(mts, N))


def find_kills(mts: list[int], N: int) -> int:
    counts = []
    kill = 0
    h = mts[0]

    for i in range(1, N):
        if mts[i] < h:
            kill += 1
        else:
            h = mts[i]
            counts.append(kill)
            kill = 0
    counts.append(kill)
    return max(counts)


if __name__ == '__main__':
    main()
