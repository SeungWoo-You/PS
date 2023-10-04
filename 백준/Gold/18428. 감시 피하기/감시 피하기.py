import sys


class Surveillance:
    def __init__(self) -> None:
        self.N: int
        self.teachers: set[tuple[int, int]] = set()
        self.students: set[tuple[int, int]] = set()
        self.empty: set[tuple[int, int]] = set()
        self.get_info()

    def get_info(self) -> None:
        self.N = int(input())
        for i in range(self.N):
            line = input().strip().split()
            for j, x in enumerate(line):
                if x == 'T':
                    self.teachers.add((i, j))
                if x == 'S':
                    self.students.add((i, j))
                if x == 'X':
                    self.empty.add((i, j))

    def avoid(self, blocks: set[tuple[int, int]] = set()) -> bool:
        if len(blocks) == 3:
            return self.is_possible(blocks)
        answer = False
        for E in self.empty:
            if E in blocks:
                continue
            blocks.add(E)
            answer |= self.avoid(blocks)
            blocks.discard(E)
        return answer

    def is_possible(self, blocks: set[tuple[int, int]]) -> bool:
        Dx = [0, 0, -1, 1]
        Dy = [-1, 1, 0, 0]
        for T in self.teachers:
            for D in zip(Dx, Dy):
                if self.check_detection(blocks, T, D) == True:
                    return False
        return True

    def check_detection(self, blocks: set[tuple[int, int]], T: tuple[int, int], D: tuple[int, int]) -> bool:
        i, j = T
        dx, dy = D
        x, y = i + dx, j + dy
        while 0 <= x < self.N and 0 <= y < self.N:
            if (x, y) in blocks:
                break
            if (x, y) in self.students:
                return True
            x, y = x + dx, y + dy
        return False


def main():
    surve = Surveillance()
    print('YES' if surve.avoid() else 'NO')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
