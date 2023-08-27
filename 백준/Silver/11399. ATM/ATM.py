def main():
    N = int(input())
    costs = list(map(int, input().split()))
    costs.sort()
    res = 0
    for x in costs:
        res += N * x
        N -= 1
    print(res)


if __name__ == '__main__':
    main()
