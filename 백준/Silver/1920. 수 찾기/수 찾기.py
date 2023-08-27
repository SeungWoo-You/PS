def main():
    N = int(input())
    ls = set(map(int, input().split()))
    M = int(input())
    nums = map(int, input().split())
    for n in nums:
        print(1 if n in ls else 0)


if __name__ == '__main__':
    main()
