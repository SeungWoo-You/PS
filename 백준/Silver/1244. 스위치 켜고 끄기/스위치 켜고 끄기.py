import sys


def main():
    N = int(input())
    switches = list(map(int, input().split()))
    S = int(input())
    for _ in range(S):
        gen, sel = map(int, input().split())
        if gen == 1:
            swt = sel
            while swt <= N:
                switches[swt - 1] = int(not switches[swt - 1])
                swt += sel
        if gen == 2:
            switches[sel - 1] = int(not switches[sel - 1])
            left, right = sel, sel
            while left >= 1 and right <= N and switches[left - 1] == switches[right - 1]:
                switches[left - 1] = int(not switches[left - 1])
                switches[right - 1] = int(not switches[right - 1])
                left -= 1
                right += 1
    for i, x in enumerate(switches, start=1):
        print(x, end=' ')
        if i % 20 == 0:
            print()


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
