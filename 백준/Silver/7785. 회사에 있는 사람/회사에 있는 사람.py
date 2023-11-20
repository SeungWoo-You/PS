import sys


def main():
    N = int(input())
    S: set[str] = set()
    for _ in range(N):
        name, state = input().strip().split()
        if state == 'enter':
            S.add(name)
        elif state == 'leave':
            S.discard(name)
    print(*sorted(S, reverse=True), sep='\n')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
