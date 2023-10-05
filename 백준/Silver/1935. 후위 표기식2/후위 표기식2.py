import sys
from numbers import Number


def main():
    N = int(input())
    expression = input().strip()
    nums = {chr(ord('A') + i): int(input()) for i in range(N)}
    S: list[str] = []
    oper = {'+', '-', '*', '/'}
    for x in expression:
        if x in oper:
            B, A = S.pop(), S.pop()
            S.append(calc(x, A, B))
        else:
            S.append(nums[x])
    print(f'{S[0]:.2f}')


def calc(oper: str, A: Number, B: Number) -> float:
    if oper == '+':
        return A + B
    if oper == '-':
        return A - B
    if oper == '*':
        return A * B
    if oper == '/':
        return A / B


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
