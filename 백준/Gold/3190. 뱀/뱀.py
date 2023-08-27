import sys
from collections import deque


class Snake:
    def __init__(self) -> None:
        self.pos = deque([(1, 1)])
        self.body = set(self.pos)
        self.direction = [0, 1]

    def move(self, N: int) -> bool:
        head = tuple(map(sum, zip(self.pos[0], self.direction)))
        x, y = head
        if 0 < x <= N and 0 < y <= N and head not in self.body:
            self.pos.appendleft(head)
            self.body.add(head)
            return True
        return False

    def eat(self, apple: set[tuple[int, int]]) -> None:
        head = self.pos[0]
        if head in apple:
            apple.discard(head)
        else:
            self.body.discard(self.pos.pop())

    def turn(self, d: str) -> None:
        dx, dy = self.direction
        if d == 'L':
            self.direction = [-dy, dx]
        elif d == 'D':
            self.direction = [dy, -dx]


class Dummy:
    def __init__(self) -> None:
        self.N: int
        self.K: int
        self.L: int
        self.apple: set[tuple[int, int]]
        self.snake: Snake
        self.info: dict[int, str] = {}
        self.get_info()

    def get_info(self) -> None:
        self.N = int(input())
        self.K = int(input())
        self.apple = set([tuple(map(int, input().split()))
                         for _ in range(self.K)])
        self.L = int(input())
        for _ in range(self.L):
            X, C = input().strip().split()
            self.info[int(X)] = C
        self.snake = Snake()

    def play(self) -> int:
        sec = 0
        snake = self.snake
        while True:
            sec += 1
            if snake.move(self.N) == False:
                break
            snake.eat(self.apple)
            if sec in self.info:
                snake.turn(self.info[sec])
        return sec


def main():
    game = Dummy()
    print(game.play())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
