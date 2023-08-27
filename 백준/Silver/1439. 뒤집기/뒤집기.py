import sys


def main():
    S = input().strip()
    count = [0, 0]
    prev = S[0]
    for x in S:
        if x != prev:
            count[int(prev)] += 1
        prev = x

    count[int(S[-1])] += 1
    print(min(count))


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
