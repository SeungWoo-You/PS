import sys


def main():
    N = int(input())
    rem = 0
    for _ in range(N):
        student, apple = map(int, input().split())
        rem += apple % student
    print(rem)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
