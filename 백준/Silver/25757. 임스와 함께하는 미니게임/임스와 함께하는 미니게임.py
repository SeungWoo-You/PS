import sys


def main():
    N, T = input().split()
    N = int(N)
    mode = {
        'Y': 1,
        'F': 2,
        'O': 3
    }
    player = set([input().strip() for _ in range(N)])
    print(len(player) // mode[T])


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
