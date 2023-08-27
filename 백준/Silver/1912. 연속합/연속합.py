import sys


def main():
    n = int(input())
    nums = list(map(int, input().split()))

    temp = [-sys.maxsize] * n
    temp[0] = nums[0]
    for j in range(1, n):
        temp[j] = max(nums[j], nums[j] + temp[j - 1])
    print(max(temp))


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
