import sys


def main():
    N, M = map(int, input().split())
    moster_no: dict[str, int] = dict()
    no_moster: dict[int, str] = dict()
    for i in range(1, N + 1):
        name = input().strip()
        moster_no[name] = i
        no_moster[i] = name

    for _ in range(M):
        x = input().strip()
        if x.isdigit():
            print(no_moster[int(x)])
        else:
            print(moster_no[x])


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
