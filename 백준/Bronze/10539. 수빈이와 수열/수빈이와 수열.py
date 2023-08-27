def main():
    N = int(input())
    seq_B = list(map(int, input().split(" ")))
    seq_nB = [(i + 1) * seq_B[i] for i in range(N)]
    res: list[int] = [seq_nB[0]]
    for i in range(1, N):
        res.append(seq_nB[i] - seq_nB[i - 1])
    print(*res)


if __name__ == '__main__':
    main()
