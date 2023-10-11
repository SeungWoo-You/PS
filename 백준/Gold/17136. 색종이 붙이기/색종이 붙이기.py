import sys


class Paper:
    def __init__(self) -> None:
        self.N = 10
        self.board: list[list[int]] = [
            list(map(int, input().split())) for _ in range(self.N)]
        self.FIN = 5

    def attach(self, pos: tuple[int, int], used: dict[int, int]) -> int:
        i, j = pos
        if i >= self.N:
            return sum(used.values())
        if j >= self.N:
            return self.attach((i + 1, 0), used)
        count = sys.maxsize
        if self.board[i][j] == 1:
            for paper, v in used.items():
                if v == self.FIN:
                    continue
                if i + paper - 1 >= self.N or j + paper - 1 >= self.N:
                    continue
                if self.check_rect((i, j), paper) == False:
                    break
                for dx in range(paper):
                    for dy in range(paper):
                        x, y = i + dx, j + dy
                        self.board[x][y] = 0
                used[paper] += 1
                count = min(count, self.attach((i, j + paper), used))
                used[paper] -= 1
                for dx in range(paper):
                    for dy in range(paper):
                        x, y = i + dx, j + dy
                        self.board[x][y] = 1
        else:
            count = min(count, self.attach((i, j + 1), used))
        return count

    def check_rect(self, pos: tuple[int, int], s: int) -> bool:
        i, j = pos
        for dx in range(s):
            for dy in range(s):
                x, y = i + dx, j + dy
                if self.board[x][y] == 0:
                    return False
        return True


def main():
    paper = Paper()
    used = {i: 0 for i in range(1, 6)}
    result = paper.attach((0, 0), used)
    print(result if result != sys.maxsize else -1)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
