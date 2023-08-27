import sys


def main():
    N = int(input())
    nums = [1] * 10
    for _ in range(1, N):
        temp = [sum(nums[:i]) for i in range(1, 11)]
        nums = temp.copy()
    print(sum(nums) % 10007)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
