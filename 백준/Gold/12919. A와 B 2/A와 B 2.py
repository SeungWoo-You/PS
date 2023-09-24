import sys


def main():
    S = list(input().strip())
    T = list(input().strip())
    print(int(change(S, T)))


def change(S: list[str], T: list[str]) -> bool:
    if S == T:
        return True
    if len(S) >= len(T):
        return False
    check = False
    if T[-1] == 'A':
        nT = T.copy()
        nT.pop()
        check |= change(S, nT)
    if T[0] == 'B':
        nT = list(reversed(T))
        nT.pop()
        check |= change(S, nT)
    return check


if __name__ == '__main__':
    input = sys.stdin.readline
    sys.setrecursionlimit(10**5)
    main()
