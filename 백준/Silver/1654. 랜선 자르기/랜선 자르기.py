def main():
    K, N = map(int, input().split())
    wires = [int(input()) for _ in range(K)]
    start = 1
    end = max(wires)

    length = 0
    while start < end:
        mid = (start + end - 1) // 2
        temp = 0
        for w in wires:
            temp += w // mid
        if temp >= N:
            length = mid
            start = mid + 1
        else:
            end = mid - 1
    if start == end:
        temp = 0
        for w in wires:
            temp += w // start
        if temp >= N:
            length = start
    print(length)


if __name__ == '__main__':
    main()
