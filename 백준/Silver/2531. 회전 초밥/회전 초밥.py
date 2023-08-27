def main():
    N, d, k, c = map(int, input().split())
    sushi = [int(input()) for _ in range(N)]
    unique = 0

    for i in range(N):
        left = i
        right = i + k
        coupon = True
        line = set()
        for i in range(left, right):
            i %= N
            line.add(sushi[i])
            if sushi[i] == c:
                coupon = False
        num = len(line)
        if coupon == True:
            num += 1
        if num > unique:
            unique = num
    print(unique)


if __name__ == '__main__':
    main()
