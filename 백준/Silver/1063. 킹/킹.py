import sys


class King:
    def __init__(self) -> None:
        self.N: int
        self.pos: str
        self.stone: str
        self.cmd: list[str]
        self.get_info()

    def get_info(self) -> None:
        self.pos, self.stone, N = input().strip().split()
        self.N = int(N)
        self.cmd = [input().strip() for _ in range(self.N)]

    def move(self) -> None:
        for cmd in self.cmd:
            pos = self.pos
            stone = self.stone
            if cmd == 'R':
                pos = chr(ord(pos[0]) + 1) + pos[1]
                if pos == stone:
                    stone = chr(ord(stone[0]) + 1) + stone[1]
            elif cmd == 'L':
                pos = chr(ord(pos[0]) - 1) + pos[1]
                if pos == stone:
                    stone = chr(ord(stone[0]) - 1) + stone[1]
            elif cmd == 'B':
                pos = pos[0] + str(int(pos[1]) - 1)
                if pos == stone:
                    stone = stone[0] + str(int(stone[1]) - 1)
            elif cmd == 'T':
                pos = pos[0] + str(int(pos[1]) + 1)
                if pos == stone:
                    stone = stone[0] + str(int(stone[1]) + 1)
            elif cmd == 'RT':
                pos = chr(ord(pos[0]) + 1) + str(int(pos[1]) + 1)
                if pos == stone:
                    stone = chr(ord(stone[0]) + 1) + str(int(stone[1]) + 1)
            elif cmd == 'LT':
                pos = chr(ord(pos[0]) - 1) + str(int(pos[1]) + 1)
                if pos == stone:
                    stone = chr(ord(stone[0]) - 1) + str(int(stone[1]) + 1)
            elif cmd == 'RB':
                pos = chr(ord(pos[0]) + 1) + str(int(pos[1]) - 1)
                if pos == stone:
                    stone = chr(ord(stone[0]) + 1) + str(int(stone[1]) - 1)
            elif cmd == 'LB':
                pos = chr(ord(pos[0]) - 1) + str(int(pos[1]) - 1)
                if pos == stone:
                    stone = chr(ord(stone[0]) - 1) + str(int(stone[1]) - 1)
            if 'A' <= pos[0] <= 'H' and 1 <= int(pos[1]) <= 8:
                if 'A' <= stone[0] <= 'H' and 1 <= int(stone[1]) <= 8:
                    self.pos = pos
                    self.stone = stone


def main():
    piece = King()
    piece.move()
    print(piece.pos, piece.stone, sep='\n')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
