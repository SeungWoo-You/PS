def main():
    S1 = input()
    S2 = input()
    M = len(S1)
    N = len(S2)
    table = [[0] * (N + 1) for _ in range(M + 1)]

    for j, y in enumerate(S2, start=1):
        for i, x in enumerate(S1, start=1):
            plus = 1 if y == x else 0
            table[i][j] = max(table[i - 1][j - 1] + plus,
                              table[i - 1][j], table[i][j - 1])
    print(table[-1][-1])


if __name__ == '__main__':
    main()
