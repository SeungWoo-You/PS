def main():
    N = int(input())
    bulks: list[tuple[int]] = []
    for _ in range(N):
        x, y = map(int, input().split())
        bulks.append((x, y))

    rank: list[int] = []
    for x1, y1 in bulks:
        now_rank = 1
        for x2, y2 in bulks:
            if x1 < x2 and y1 < y2:
                now_rank += 1
        rank.append(now_rank)
    print(*rank, sep=' ')


if __name__ == '__main__':
    main()
