import sys
import heapq


def main():
    N = int(input())
    LH: list[int] = []
    RH: list[int] = []
    for _ in range(N):
        x = int(input())
        if len(LH) >= len(RH):
            if not LH:
                heapq.heappush(LH, -x)
            else:
                if x >= -LH[0]:
                    heapq.heappush(RH, x)
                else:
                    heapq.heappush(RH, -heapq.heappop(LH))
                    heapq.heappush(LH, -x)
        else:
            if x < RH[0]:
                heapq.heappush(LH, -x)
            else:
                heapq.heappush(LH, -heapq.heappop(RH))
                heapq.heappush(RH, x)
        print(-LH[0] if len(LH) >= len(RH) else RH[0])


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
