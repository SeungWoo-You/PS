def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    res = [a for a in A if a < X]
    print(*res)


if __name__ == '__main__':
    main()
