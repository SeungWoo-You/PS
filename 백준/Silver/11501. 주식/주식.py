def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        stocks = list(map(int, input().split()))
        stocks.reverse()

        s_max = 0
        benefit = 0
        for n in stocks:
            if s_max < n:
                s_max = n
            elif s_max > n:
                benefit += s_max - n
            else:
                continue
        print(benefit)


if __name__ == '__main__':
    main()
