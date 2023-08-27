def main():
    N = int(input())
    res_num = 0
    res_seq: list[int] = []
    for n in range(1, N + 1):
        seq = [N, n]
        while seq[-2] - seq[-1] >= 0:
            seq.append(seq[-2] - seq[-1])
        if len(seq) > res_num:
            res_num = len(seq)
            res_seq = seq.copy()
    print(res_num)
    print(*res_seq)


if __name__ == '__main__':
    main()
