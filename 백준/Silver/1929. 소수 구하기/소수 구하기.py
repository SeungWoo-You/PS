def main():
    M, N = map(int, input().split())
    nums = set(range(M, N + 1)) if M != 1 else set(range(2, N + 1))

    nums.difference_update()
    for x in range(2, N + 1):
        nums.difference_update(set(range(2 * x, N + 1, x)))
    print(*nums, sep='\n')


if __name__ == '__main__':
    main()
