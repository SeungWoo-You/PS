def main():
    N = int(input())
    n = 0
    prev = 0
    while True:
        temp = room(n)
        if prev < N <= temp:
            break
        prev = temp
        n += 1
    print(n + 1)


def room(n: int) -> int:
    return 3 * n * (n + 1) + 1


if __name__ == '__main__':
    main()
