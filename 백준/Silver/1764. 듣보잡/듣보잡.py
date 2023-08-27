import sys


def main():
    N, M = map(int, input().split())
    p1 = set([input().strip() for _ in range(N)])
    p2 = set([input().strip() for _ in range(M)])
    inter = p1.intersection(p2)
    print(len(inter))
    print(*sorted(inter), sep='\n')


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
