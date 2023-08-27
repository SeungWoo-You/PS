import sys


def main():
    T = int(input())
    for _ in range(T):
        sym = input().strip().split()
        k = float(sym[0])
        for cmd in sym[1:]:
            if cmd == '@':
                k *= 3
            elif cmd == '%':
                k += 5
            elif cmd == '#':
                k -= 7
        print(f'{k:.2f}')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
