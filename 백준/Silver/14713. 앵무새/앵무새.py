import sys
from collections import deque

def main():
    N = int(input())
    S = [deque(input().strip().split()) for _ in range(N)]
    L = deque(input().strip().split())
    while L:
        for Q in S:
            if Q and L[0] == Q[0]:
                L.popleft()
                Q.popleft()
                break
        else:
            print('Impossible')
            return
    for Q in S:
        if Q:
            print('Impossible')
            return
    print('Possible')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
