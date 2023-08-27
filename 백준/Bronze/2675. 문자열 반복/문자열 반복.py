def main():
    T = int(input())
    for _ in range(T):
        R, S = input().split()
        R = int(R)
        for x in S:
            print(x * R, end='')
        print("")


if __name__ == '__main__':
    main()
