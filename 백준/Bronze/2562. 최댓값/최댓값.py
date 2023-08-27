def main():
    N = 9
    M = 0
    idx = 1
    for i in range(N):
        m = int(input())
        if m > M:
            M = m
            idx = i + 1
    print(M, idx, sep='\n')


if __name__ == '__main__':
    main()
