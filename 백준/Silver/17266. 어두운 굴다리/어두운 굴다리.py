import sys


def main():
    N = int(input())
    M = int(input())
    lamp = list(map(int, input().split()))
    start = 1
    end = N
    while start < end:
        mid = (start + end) // 2
        area = [max(0, lamp[0] - mid), lamp[0] + mid]
        if area[0] == 0:
            for lgt in lamp:
                if area[1] < lgt - mid:
                    break
                area[1] = lgt + mid
            else:
                if area[1] >= N:
                    end = mid
                    continue
        start = mid + 1
    print(start)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
