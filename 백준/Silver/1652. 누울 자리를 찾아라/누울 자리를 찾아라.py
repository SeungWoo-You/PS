def main():
    N = int(input())
    room = [input() for _ in range(N)]
    row = find_space(room)
    room_reverse = []
    for gp in zip(*room):
        room_reverse.append(''.join(gp))
    col = find_space(room_reverse)
    print(row, col)


def find_space(room: list[str]) -> int:
    res = 0
    for l in room:
        spaces = l.split('X')
        res += len(list(filter(lambda x: len(x) >= 2, spaces)))
    return res


if __name__ == '__main__':
    main()
