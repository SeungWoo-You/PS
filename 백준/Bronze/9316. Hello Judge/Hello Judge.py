import sys


def main():
    N = int(input())
    for i in range(1, N + 1):
        print(f"Hello World, Judge {i}!")


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
