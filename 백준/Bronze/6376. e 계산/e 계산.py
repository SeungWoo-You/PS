import sys


def main():
    aprx = 0
    temp = 1
    print('n e')
    print('- -----------')
    for n in range(10):
        temp = factorial_sum(n, temp)
        aprx += temp
        if n == 0 or n == 1:
            print(f'{n} {aprx:.0f}')
        elif n == 2:
            print(f'{n} {aprx:.1f}')
        else:
            print(f'{n} {aprx:.9f}')


def factorial_sum(n: int, prev: float) -> float:
    return prev / n if n != 0 else 1


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
