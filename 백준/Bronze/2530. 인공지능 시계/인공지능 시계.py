def main():
    H, M, S = map(int, input().split())
    sec = int(input())
    m, s = divmod(S + sec, 60)
    h, m = divmod(M + m, 60)
    h = (H + h) % 24
    print(h, m, s)


if __name__ == '__main__':
    main()
