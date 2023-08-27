import sys
import heapq


def main():
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    H = [table[i][0] for i in range(N)]
    heapq.heapify(H)

    for j in range(1, N):
        for i in range(N - 1, -1, -1):
            if table[i][j] < H[0]:
                break
            else:
                heapq.heappop(H)
                heapq.heappush(H, table[i][j])
    print(H[0])


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
