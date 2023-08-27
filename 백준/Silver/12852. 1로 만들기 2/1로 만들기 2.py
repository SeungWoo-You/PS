def main():
    N = int(input())
    count = [0 for _ in range(N + 3)]
    count[2] = count[3] = 1
    nums = [[], [1], [1, 2], [1, 3]]

    for n in range(4, N + 1):
        quot3, rem3 = divmod(n, 3)
        quot2, rem2 = divmod(n, 2)
        minus_1 = n - 1
        if rem3 == 0 and rem2 == 0:
            choice = min(count[quot3], count[quot2], count[minus_1])
            target = quot3 if choice == count[quot3] else (
                quot2 if choice == count[quot2] else minus_1)
        elif rem3 == 0:
            choice = min(count[quot3], count[minus_1])
            target = quot3 if choice == count[quot3] else minus_1
        elif rem2 == 0:
            choice = min(count[quot2], count[minus_1])
            target = quot2 if choice == count[quot2] else minus_1
        else:
            choice = count[n - 1]
            target = minus_1
            count[n] = count[n - 1] + 1
        count[n] = choice + 1
        nums.append(nums[target] + [n])
    print(count[N])
    print(*reversed(nums[N]))


if __name__ == '__main__':
    main()
