def main():
    N = int(input())
    print(get_bags(N))


def get_bags(N: int) -> int:
    sugars = [-1, -1, -1, 1, -1, 1]
    for s in range(6, N + 1):
        if sugars[s - 5] != -1:
            sugars.append(sugars[s - 5] + 1)
        elif sugars[s - 3] != -1:
            sugars.append(sugars[s - 3] + 1)
        else:
            sugars.append(-1)
    return sugars[-1] if N >= 5 else sugars[N]


if __name__ == '__main__':
    main()
