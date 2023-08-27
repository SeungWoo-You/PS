def main():
    N = int(input())
    count = [0 for _ in range(N + 3)]
    count[2] = count[3] = 1
    for n in range(4, N + 1):
        quot3, rem3 = divmod(n, 3)
        quot2, rem2 = divmod(n, 2)
        minus_1 = n - 1
        if rem3 == 0 and rem2 == 0:
            count[n] = min(count[quot3], count[quot2], count[minus_1]) + 1
        elif rem3 == 0:
            count[n] = min(count[quot3], count[minus_1]) + 1
        elif rem2 == 0:
            count[n] = min(count[quot2], count[minus_1]) + 1
        else:
            count[n] = count[n - 1] + 1
    print(count[N])


if __name__ == '__main__':
    main()
