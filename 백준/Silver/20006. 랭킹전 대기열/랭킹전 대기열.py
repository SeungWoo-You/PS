
import sys


def main():
    p, m = map(int, input().split())
    players: list[tuple[int, str]] = []
    for _ in range(p):
        info = input().strip().split()
        players.append((int(info[0]), info[1]))
    rooms: list[list[tuple[int, str]]] = []
    for user in players:
        R: list[tuple[int, str]] = []
        for r in rooms:
            if len(r) < m and r[0][0] - 10 <= user[0] <= + r[0][0] + 10:
                R = r
                break
        if not R:
            rooms.append(R)
        R.append(user)
    for r in rooms:
        print('Started!' if len(r) == m else 'Waiting!')
        for u in sorted(r, key=lambda p: p[1]):
            print(*u)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
