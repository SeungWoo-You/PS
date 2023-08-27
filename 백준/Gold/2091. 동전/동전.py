import sys


def main():
    X, A, B, C, D = map(int, input().split())
    coins = Coins(X, A, B, C, D)
    rem = X % 5
    if A < rem:
        print(*coins.used)
        return
    temp = [rem, 0, 0, 0]
    money = rem
    coins.put(money, money, temp)
    print(*coins.used)


class Coins:
    def __init__(self, X: int, cent: int, nickel: int, dime: int, quarter: int) -> None:
        self.X = X
        self.cent = cent
        self.nickel = nickel
        self.dime = dime
        self.quarter = quarter
        self.total = [-1] * 10001
        self.used = [0] * 4

    def put(self, money: int, count: int, temp: list[int]) -> None:
        if self.total[money] >= count:
            return
        if money == self.X:
            self.total[money] = count
            self.used = temp.copy()
            return

        self.total[money] = count
        if self.cent >= temp[0] + 5 and money + 5 <= self.X:
            temp[0] += 5
            self.put(money + 5, count + 5, temp)
            temp[0] -= 5
        if self.nickel > temp[1] and money + 5 <= self.X:
            temp[1] += 1
            self.put(money + 5, count + 1, temp)
            temp[1] -= 1
        if self.dime > temp[2] and money + 10 <= self.X:
            temp[2] += 1
            self.put(money + 10, count + 1, temp)
            temp[2] -= 1
        if self.quarter > temp[3] and money + 25 <= self.X:
            temp[3] += 1
            self.put(money + 25, count + 1, temp)
            temp[3] -= 1


if __name__ == "__main__":
    input = sys.stdin.readline
    sys.setrecursionlimit(10**5)
    main()
