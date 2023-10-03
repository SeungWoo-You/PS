import sys


class Light:
    def __init__(self) -> None:
        self.N: int
        self.given: list[int]
        self.final: list[int]
        self.get_info()

    def get_info(self) -> None:
        self.N = int(input())
        self.given = list(map(int, list(input().strip())))
        self.final = list(map(int, list(input().strip())))

    def change(self, status: list[int], i: int) -> None:
        status[i] = abs(status[i] - 1)

    def count(self, zero_on: bool) -> int:
        answer = sys.maxsize
        temp = 0
        status = self.given.copy()
        if zero_on == True:
            temp = 1
            self.change(status, 0)
            self.change(status, 1)
        for i in range(1, self.N):
            if self.final[i - 1] != status[i - 1]:
                temp += 1
                self.change(status, i - 1)
                self.change(status, i)
                if i != self.N - 1:
                    self.change(status, i + 1)
        if status[-1] == self.final[-1]:
            answer = min(answer, temp)
        return answer


def main():
    light = Light()
    answer = light.count(True)
    answer = min(answer, light.count(False))
    print(answer if answer != sys.maxsize else -1)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
