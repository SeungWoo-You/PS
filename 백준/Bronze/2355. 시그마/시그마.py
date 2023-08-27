import sys


def main():
    A, B = sorted(map(int, input().split()))
    if A <= 0 and B > 0:
        start = abs(A + B)
        end = abs(A)
        S2 = end * (end + 1) // 2
        S1 = start * (start + 1) // 2
        res = -(S2 - S1) if abs(A) - B > 0 else S2 - S1
    if A <= 0 and B <= 0:
        start = abs(B) - 1
        end = abs(A)
        S2 = end * (end + 1) // 2
        S1 = start * (start + 1) // 2
        res = -(S2 - S1)
    else:
        start = A - 1
        end = B
        S2 = end * (end + 1) // 2
        S1 = start * (start + 1) // 2
        res = S2 - S1
    print(res)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
