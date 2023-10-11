import sys
from collections import defaultdict, Counter


def main():
    T = int(input())
    for _ in range(T):
        S = input().strip()
        K = int(input())
        game1 = sys.maxsize
        game2 = -sys.maxsize
        count = Counter(S)
        char_pos: defaultdict[str, list[int]] = defaultdict(list)
        for i, c in enumerate(S):
            if count[c] >= K:
                char_pos[c].append(i)
        for c, ls in char_pos.items():
            i = 0
            for j in range(K - 1, len(ls)):
                L = ls[j] - ls[i] + 1
                game1 = min(game1, L)
                game2 = max(game2, L)
                i += 1
        if game1 == sys.maxsize or game2 == -sys.maxsize:
            print(-1)
        else:
            print(game1, game2)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
