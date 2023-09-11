import sys


def main():
    N = int(input())
    d = 0
    while N > 0:
        d += 1
        N -= d
    nume = d + N if d % 2 == 0 else -N + 1
    deno = d - nume + 1 if d % 2 == 0 else d + N
    print(f'{nume}/{deno}')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
