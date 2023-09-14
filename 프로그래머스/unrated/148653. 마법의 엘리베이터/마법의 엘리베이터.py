import sys
sys.setrecursionlimit(10**5)

class Elevator:
    def __init__(self, storey: int) -> None:
        self.S: int = storey
    
    def downside(self, c: int, S: int) -> int:
        rem = (S // 10**c) % 10
        if c > 9:
            return rem
        else:
            round_up = self.downside(c + 1, S + (10 - rem) * 10**c)
            round_down = self.downside(c + 1, S - rem * 10**c)
            answer = min(round_up + 10 - rem, round_down + rem)
            return answer

def solution(storey):
    elev = Elevator(storey)
    return elev.downside(0, storey)

