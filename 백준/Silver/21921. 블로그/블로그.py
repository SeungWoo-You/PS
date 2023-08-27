import sys


def main():
    N, X = map(int, input().split())
    visiter = list(map(int, input().split()))
    count = 0
    for j in range(X):
        count += visiter[j]
    same = 1
    i = 0
    partial = count
    for j in range(X, N):
        partial = partial - visiter[i] + visiter[j]
        if partial == count:
            same += 1
        elif partial > count:
            count = partial
            same = 1
        i += 1
    if count == 0:
        print('SAD')
        return
    else:
        print(count)
        print(same)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
