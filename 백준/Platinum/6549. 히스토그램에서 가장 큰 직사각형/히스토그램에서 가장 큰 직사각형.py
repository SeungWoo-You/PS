def main():
    line = input()
    while line != '0':
        puts = list(map(int, line.split()))
        N = puts[0]
        histo: list[tuple[int]] = []
        for i in range(N):
            h = puts[i + 1]
            histo.append((i, i + 1, h))
        print(find_area(histo, N))
        line = input()


def find_area(histo: list[int], N: int) -> int:
    i = 0
    heights: list[int] = []
    area = 0
    while i < N:
        l, r, y = histo[i]
        if not heights or heights[-1][2] < y:
            heights.append((l, r, y))
            i += 1
        else:
            top = heights.pop()[2]
            side = l - heights[-1][1] if heights else l
            area = max(area, top * side)
    while heights:
        top = heights.pop()[2]
        side = N - heights[-1][1] if heights else N
        area = max(area, top * side)
    return area


if __name__ == '__main__':
    main()
