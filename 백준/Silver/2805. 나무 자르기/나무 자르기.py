import sys


def main():
    N, M = map(int, input().split())
    trees = list(map(int, input().split()))
    start = 1
    end = max(trees)
    cuts = 0
    while start < end:
        mid = (end + start) // 2
        temp_cut = 0
        for t in trees:
            temp_cut += max(0, t - mid)
        if temp_cut >= M:
            cuts = max(cuts, mid)
            start = mid + 1
        else:
            end = mid - 1
    if start == end:
        mid = start
        temp_cut = 0
        for t in trees:
            temp_cut += max(0, t - mid)
        if temp_cut >= M:
            cuts = max(cuts, mid)
    print(cuts)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
