import sys
import heapq


def main():
    N, M, K = map(int, sys.stdin.readline().split())
    beers = [list(map(int, input().split())) for _ in range(K)]
    beers = sorted(beers, key=lambda c: c[1])
    pref = 0
    choice: list[int] = []
    for x in beers:
        heapq.heappush(choice, x[0])
        pref += x[0]
        if len(choice) == N:
            if pref >= M:
                print(x[1])
                return
            else:
                pref -= heapq.heappop(choice)
    print(-1)


if __name__ == '__main__':
    main()
