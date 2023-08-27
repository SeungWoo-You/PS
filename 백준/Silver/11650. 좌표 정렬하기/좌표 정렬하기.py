def main():
    N = int(input())
    ls: list[tuple[int]] = []
    for _ in range(N):
        pt = tuple(map(int, input().split()))
        ls.append(pt)
    ls.sort()
    for p in ls:
        print(*p)


if __name__ == '__main__':
    main()
