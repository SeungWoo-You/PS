import sys
from collections import defaultdict, deque


class City:
    def __init__(self) -> None:
        self.N: int
        self.M: int
        self.K: int
        self.X: int
        self.board: defaultdict[int, set[int]] = defaultdict(set)
        self.get_info()

    def get_info(self) -> None:
        self.N, self.M, self.K, self.X = map(int, input().split())
        for _ in range(self.M):
            u, v = map(int, input().split())
            self.board[u].add(v)

    def find(self) -> list[int]:
        checked: set[int] = set()
        answer: list[int] = []
        Q: deque[tuple[int, int]] = deque([(0, self.X)])
        while Q:
            d, u = Q.popleft()
            if u in checked:
                continue
            checked.add(u)
            if d == self.K:
                answer.append(u)
            Q.extend([(d + 1, v) for v in self.board[u]])
        return answer


def main():
    city = City()
    answer = city.find()
    if not answer:
        print(-1)
    else:
        print(*sorted(answer), sep='\n')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
