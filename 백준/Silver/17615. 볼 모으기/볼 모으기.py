import sys
from itertools import product


def main():
    N = int(input())
    balls = list(input().strip())
    way = ['front', 'back']
    color = ['R', 'B']
    count = sys.maxsize
    for c, w in product(color, way):
        count = min(count, grouping(balls, c, w))
    print(count)


def grouping(balls: list[str], color: str, way: str) -> int:
    count = 0
    part = 0
    iteration = balls if way == 'front' else reversed(balls)
    for b in iteration:
        if b == color:
            part += 1
        else:
            count += part
            part = 0
    return count


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
