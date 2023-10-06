import sys


def main():
    N, T, P = map(int, input().split())
    ranking = list(map(int, input().split())) if N > 0 else []
    ranking.append(T)
    ranking.sort(reverse=True)
    while len(ranking) > P:
        X = ranking[-1]
        while ranking:
            if ranking[-1] == X:
                ranking.pop()
            else:
                break
    try:
        print(ranking.index(T) + 1)
    except:
        print(-1)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
