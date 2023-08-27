def main():
    N, K = map(int, input().split())
    ls = [list(map(int, input().split())) for _ in range(N)]
    ls.sort(key=lambda l: (-l[1], -l[2], -l[3]))

    rank = 1
    for i, l in enumerate(ls):
        if i == 0 or ls[i - 1][1:] == l[1:]:
            pass
        else:
            rank += 1
        if l[0] == K:
            break
    print(rank)


if __name__ == '__main__':
    main()
