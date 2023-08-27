def main():
    N = int(input())
    s = set(map(int, input().split()))
    print(min(s), max(s))


if __name__ == '__main__':
    main()
