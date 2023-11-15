import sys


def main():
    N = int(input())
    count = 0
    for x in range(1, N + 1):
        for j in str(x):
            if j in {'3', '6', '9'}:
                count += 1
    print(count)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
