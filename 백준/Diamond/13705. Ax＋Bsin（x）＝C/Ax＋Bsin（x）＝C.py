from decimal import *


def main():
    global A, B, C, PI
    getcontext().prec = 60
    getcontext().rounding = ROUND_HALF_UP
    A, B, C = map(Decimal, input().split())
    PI = Decimal('3.14159265358979323846264338327950288419716939937510')
    print(round(find_sol(), 6))


def sin(x: Decimal) -> Decimal:
    x = x % (2 * PI)
    i, lasts, s, fact, num, sign = 1, 0, x, 1, x, 1
    while s != lasts:
        lasts = s
        i += 2
        fact *= i * (i - 1)
        num *= x * x
        sign *= -1
        s += num / fact * sign
    return +s


def f(t: Decimal) -> Decimal:
    return A * t + B * sin(t)


def find_sol():
    upper = Decimal('2000000')
    lower = Decimal('0')

    while abs(upper - lower) > Decimal(10**-25):
        mid = (upper + lower) / 2
        if f(mid) < C:
            lower = mid
        else:
            upper = mid

    return upper


if __name__ == '__main__':
    main()
