import sys


def main():
    n = int(input())
    nums = list(map(int, input().split()))

    temp = [[-sys.maxsize] * n for _ in range(2)]
    temp[0][0] = nums[0]
    res = -sys.maxsize
    for j in range(1, n):
        temp[0][j] = max(nums[j], nums[j] + temp[0][j - 1])
        temp[1][j] = max(temp[0][j - 1], temp[1][j - 1] + nums[j])
    res = max(res, max(temp[0]), max(temp[1]))
    print(res)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
