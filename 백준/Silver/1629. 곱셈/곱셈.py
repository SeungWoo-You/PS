import sys


def main():
    A, B, C = map(int, input().split())
    print(multiple(A, B, C))


def multiple(A: int, B: int, C: int) -> int:
    if B < 3:
        return A**B % C
    elif B % 2 == 0:
        return multiple(multiple(A, B // 2, C) % C, 2, C) % C
    else:
        return multiple(multiple(A, (B - 1) // 2, C) % C, 2, C) * A % C


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
