import sys
from collections import deque
import heapq


def main():
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        order = list(map(int, input().split()))
        signs = deque(zip(order, range(N)))
        order = [-x for x in order]
        heapq.heapify(order)

        count = 1
        while order:
            s = signs.popleft()
            if s[0] == -order[0]:
                if s[1] == M:
                    print(count)
                    break
                heapq.heappop(order)
                count += 1
            else:
                signs.append(s)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
