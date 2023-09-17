import sys


class Equation:
    def __init__(self) -> None:
        self.N: int
        self.E: str
        self.eq: list[str] = []
        self.M = -sys.maxsize
        self.get_info()

    def get_info(self) -> None:
        N = int(input())
        self.E = input().strip()
        self.divide()
        self.N = len(self.eq)

    def find(self, i: int, val: int) -> None:
        if i == self.N - 1:
            self.M = max(self.M, val)
            return
        if i + 2 < self.N:
            front = self.operate(val, self.eq[i + 1], self.eq[i + 2])
            self.find(i + 2, front)
        if i + 4 < self.N:
            rear = self.operate(self.eq[i + 2], self.eq[i + 3], self.eq[i + 4])
            front = self.operate(val, self.eq[i + 1], rear)
            self.find(i + 4, front)

    def divide(self) -> None:
        x = ''
        nums: set[str] = set(map(str, range(10)))
        for c in self.E:
            if c in nums:
                x += c
            else:
                self.eq.append(x)
                self.eq.append(c)
                x = ''
        self.eq.append(x)
        return

    def operate(self, x: int | str, o: str, y: int | str) -> int:
        x, y = int(x), int(y)
        if o == '+':
            return x + y
        if o == '-':
            return x - y
        if o == '*':
            return x * y


def main():
    eq = Equation()
    eq.find(0, int(eq.eq[0]))
    print(eq.M)


if __name__ == '__main__':
    sys.setrecursionlimit(10**5)
    input = sys.stdin.readline
    main()
