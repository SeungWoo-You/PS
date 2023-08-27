def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        count_2 = 0
        count_5 = 0
        i = 2
        j = 5
        while i <= N:
            count_2 += N // i
            i *= 2
        while j <= N:
            count_5 += N // j
            j *= 5
        print(min(count_2, count_5))


if __name__ == '__main__':
    main()
