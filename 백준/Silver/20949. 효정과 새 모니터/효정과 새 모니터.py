def main():
    N = int(input())
    ls: list[int] = []
    for i in range(N):
        w, h = map(int, input().split())
        ls.append([calc_subPPI(w, h), i + 1])
    ls.sort(key=lambda x: (-x[0], x[1]))
    res = [ls[p][1] for p in range(N)]
    print(*res, sep='\n')


def calc_subPPI(w: int, h: int) -> int:
    return w**2 + h**2


if __name__ == '__main__':
    main()
