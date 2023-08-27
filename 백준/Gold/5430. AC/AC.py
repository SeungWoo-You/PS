import sys
from collections import deque


def main():
    T = int(input())
    for _ in range(T):
        p = input().strip()
        n = int(input())
        try:
            ls = deque(map(int, input().lstrip('[').rstrip(']\n').split(',')))
        except:
            ls = []
        way = True
        for cmd in p:
            if cmd == 'R':
                way = not way
            elif cmd == 'D':
                try:
                    if way == True:
                        ls.popleft()
                    else:
                        ls.pop()
                except:
                    print('error')
                    break
        else:
            print('[', end='')
            out = ls if way == True else reversed(ls)
            print(*out, sep=',', end='')
            print(']')


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
