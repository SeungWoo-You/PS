import sys


def main():
    M = int(input())
    S = set()
    for _ in range(M):
        line = sys.stdin.readline().strip().split()
        if len(line) == 1:
            if line[0] == 'all':
                S = set(range(1, 21))
            else:
                S.clear()
            continue

        cmd, x = line
        x = int(x)
        if cmd == 'add':
            S.add(x)
        elif cmd == 'remove':
            S.discard(x)
        elif cmd == 'check':
            print(1 if x in S else 0)
        elif cmd == 'toggle':
            S.discard(x) if x in S else S.add(x)


if __name__ == '__main__':
    main()
