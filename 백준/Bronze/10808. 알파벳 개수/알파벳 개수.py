import sys
from collections import Counter


def main():
    S = Counter(input().strip())
    for i in range(26):
        c = chr(ord('a') + i)
        print(S[c] if c in S else 0, end=' ')


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
