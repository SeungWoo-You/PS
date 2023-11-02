import sys


def main():
    N = int(input())
    A = list(map(int, input().split()))
    stacks = [[] for _ in range(4)]
    for a in A:
        for s in stacks:
            if not s or s[-1] < a:
                s.append(a)
                break
        else:
            print('NO')
            return
    print('YES')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
