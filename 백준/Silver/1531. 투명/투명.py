def main():
    N, M = map(int, input().split(" "))
    SIZE = 101
    grid = [[0] * SIZE for _ in range(SIZE)]
    for _ in range(N):
        x1, y1, x2, y2 = map(int, input().split(" "))
        for x in range(x1, x2 + 1):
            for y in range(y1, y2 + 1):
                grid[x][y] += 1
    count = 0
    for x in range(1, SIZE):
        for y in range(1, SIZE):
            if grid[x][y] > M:
                count += 1
                
    print(count)

if __name__ == '__main__':
    main()
