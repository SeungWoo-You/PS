def main():
    N = int(input())
    ls: list[int] = []
    for _ in range(N):
        ls.append(int(input()))
    print(*sorted(ls), sep='\n')


if __name__ == '__main__':
    main()
