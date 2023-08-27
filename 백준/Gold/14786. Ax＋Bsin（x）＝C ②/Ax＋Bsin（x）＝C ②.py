import sys
import math


def main():
    global A, B, C
    A, B, C = map(int, input().split())
    print(f'{find_sol(C / (A + B)):.20f}')


def f(t: float) -> float:
    return A * t + B * math.sin(t) - C


def f_deriv(t: float) -> float:
    return A + B * math.cos(t)


def find_sol(t: float) -> float:
    t_next = - f(t) / f_deriv(t) + t

    if abs(t_next - t) < 10**-10:
        return t_next
    else:
        return find_sol(t_next)


if __name__ == '__main__':
    sys.setrecursionlimit(10**5)
    main()
