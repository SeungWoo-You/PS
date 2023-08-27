def main():
    N = int(input())
    ls = list(map(int, input().split()))
    print(*sorted(ls))


if __name__ == '__main__':
    main()
