import sys
import heapq


def main():
    N, K = map(int, input().split())
    gems = [tuple(map(int, input().split())) for _ in range(N)]
    bags = [int(input()) for _ in range(K)]
    bags.sort()

    heapq.heapify(gems)
    value = 0

    val_max: list[int] = []
    for b in bags:
        while gems and b >= gems[0][0]:
            G = heapq.heappop(gems)
            heapq.heappush(val_max, -G[1])
        if val_max:
            value += -heapq.heappop(val_max)
    print(value)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
