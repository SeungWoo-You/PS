import sys
import re


def main():
    N = int(input())
    lines = [input().rstrip() for _ in range(N)]
    pattern = '[a-z]+'
    ls: list[int] = []
    for row in lines:
        nums = re.split(pattern, row)
        for c in nums:
            try:
                ls.append(int(c))
            except:
                pass
    print(*sorted(ls), sep='\n')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
