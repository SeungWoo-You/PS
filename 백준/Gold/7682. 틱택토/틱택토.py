import sys


class TicTacToe:
    def __init__(self, board: str) -> None:
        self.board: list[str] = [board[3 * i:3 * (i + 1)] for i in range(3)]
        self.turn: str
        self.remain: bool = False

    def find_turn(self) -> bool:
        X, O = 0, 0
        for row in self.board:
            for p in row:
                if p == 'X':
                    X += 1
                elif p == 'O':
                    O += 1
                elif p == '.':
                    self.remain = True
        if X == O:
            self.turn = 'O'
            return True
        elif X == O + 1:
            self.turn = 'X'
            return True
        return False

    def ispossible(self) -> bool:
        if self.find_turn() == False:
            return False
        possible = {'XXX': 0, 'OOO': 0}
        for i in range(3):
            T = self.board[i]
            if T in possible:
                possible[T] += 1
        for j in range(3):
            T = ''.join([self.board[i][j] for i in range(3)])
            if T in possible:
                possible[T] += 1
        for i in {0, 2}:
            T = ''.join(self.board[abs(i - j)][j] for j in range(3))
            if T in possible:
                possible[T] += 1
        if possible['XXX'] == 0 and possible['OOO'] == 0 and self.remain == False:
            return True
        if possible['XXX'] and possible['OOO'] == 0 and self.turn == 'X':
            return True
        if possible['OOO'] and possible['XXX'] == 0 and self.turn == 'O':
            return True
        return False


def main():
    line = input().strip()
    while line != 'end':
        game = TicTacToe(line)
        print('valid' if game.ispossible() else 'invalid')
        line = input().strip()


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
