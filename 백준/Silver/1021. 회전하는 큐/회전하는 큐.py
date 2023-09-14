import sys
from collections import deque


def main():
    N, M = map(int, input().split())
    pos = list(map(int, input().split()))
    Q = deque(range(1, N + 1))
    count = 0
    for x in pos:
        left = Q.copy()
        l_cnt = 0
        while left[0] != x:
            left.append(left.popleft())
            l_cnt += 1
        right = Q.copy()
        r_cnt = 0
        while right[0] != x:
            right.appendleft(right.pop())
            r_cnt += 1
        if l_cnt < r_cnt:
            count += l_cnt
            Q = left
        else:
            count += r_cnt
            Q = right
        Q.popleft()
    print(count)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
