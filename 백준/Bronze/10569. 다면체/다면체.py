import sys


def main():
    T = int(input())
    for _ in range(T):
        V, E = map(int, input().split())
        print(2 - V + E)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
