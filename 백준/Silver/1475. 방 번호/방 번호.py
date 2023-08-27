import sys
from collections import Counter
from math import ceil


def main():
    N = int(input())
    nums = Counter(map(int, list(str(N))))
    nums[6] += nums[9]
    needs = 0
    for i, v in nums.items():
        if i == 6 or i == 9:
            needs = max(needs, ceil(v / 2))
        else:
            needs = max(needs, v)
    print(needs)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
