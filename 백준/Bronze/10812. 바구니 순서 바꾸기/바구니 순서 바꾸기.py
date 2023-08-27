def main():
    N, M = map(int, input().split(" "))
    baskets = list(range(N + 1))
    for _ in range(M):
        start, end, mid = map(int, input().split(" "))
        l_remain, left, right, r_remain = baskets[:start], baskets[start:
                                                                   mid], baskets[mid:end + 1], baskets[end + 1:]
        baskets = l_remain + right + left + r_remain
    del baskets[0]
    print(*baskets)


if __name__ == '__main__':
    main()
