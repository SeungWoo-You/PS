def main():
    N = int(input())
    res = 0
    for x in range(1, N):
        gen = x + sum(map(int, list(str(x))))
        if gen == N:
            res = x
            break
    print(res)


if __name__ == '__main__':
    main()
