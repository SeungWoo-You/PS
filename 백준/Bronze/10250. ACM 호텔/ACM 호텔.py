def main():
    T = int(input())
    for _ in range(T):
        H, W, N = map(int, input().split())
        quot, rem = divmod(N, H)
        room = quot + 1 if rem != 0 else quot
        floor = rem if rem != 0 else H
        print(str(floor) + str(room).zfill(2))


if __name__ == '__main__':
    main()
