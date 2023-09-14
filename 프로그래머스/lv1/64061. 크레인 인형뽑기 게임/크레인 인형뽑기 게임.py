class Game:
    def __init__(self, board, moves) -> None:
        self.board: list[list[int]] = board
        self.moves: list[int] = moves
    
    def play(self) -> int:
        stack: list[int] = []
        answer = 0
        for crain in self.moves:
            crain -= 1
            doll = 0
            for i in range(len(self.board)):
                if self.board[i][crain] != 0:
                    doll = self.board[i][crain]
                    self.board[i][crain] = 0
                    break
            if doll == 0:
                continue
            if stack and stack[-1] == doll:
                stack.pop()
                answer += 2
            else:
                stack.append(doll)
                continue
        return answer

def solution(board, moves):
    game = Game(board, moves)
    return game.play()