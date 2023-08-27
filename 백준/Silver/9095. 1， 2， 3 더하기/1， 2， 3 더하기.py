import sys


def main():
    T = int(input())
    res = {
        1: [[1]],
        2: [[1, 1], [2]],
        3: [[1, 1, 1], [1, 2], [2, 1], [3]]
    }
    last = 3
    for _ in range(T):
        n = int(input())
        if n <= last:
            print(len(res[n]))
            continue
        while last < n:
            last += 1
            S = []
            for k in range(last - 3, last):
                S.extend([seq.copy() + [last - k] for seq in res[k]])
            res[last] = S
        print(len(res[n]))


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
