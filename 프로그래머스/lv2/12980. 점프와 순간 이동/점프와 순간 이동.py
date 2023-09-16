import sys
sys.setrecursionlimit(10**5)

def solution(n):
    return find(n)

def find(n) -> int:
    if n == 1:
        return 1
    if n % 2 == 0:
        return find(n // 2)
    else:
        return find((n - 1) // 2) + 1