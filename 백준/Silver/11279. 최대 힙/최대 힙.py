import sys
import heapq


def main():
    N = int(input())
    max_heap: list[int] = []
    for _ in range(N):
        x = int(input())
        if x == 0:
            try:
                print(-heapq.heappop(max_heap))
            except:
                print(0)
        else:
            heapq.heappush(max_heap, -x)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
