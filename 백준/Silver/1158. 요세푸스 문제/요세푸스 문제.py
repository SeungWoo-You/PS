import sys


def main():
    N, K = map(int, input().split())
    ls = list(range(1, N + 1))
    seq: list[int] = []
    idx = 0
    while ls:
        idx = (idx + K - 1) % len(ls)
        seq.append(ls.pop(idx))
    ans = str(seq)
    print_change = {'[': '<', ']': '>'}
    print(ans.translate(ans.maketrans(print_change)))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
