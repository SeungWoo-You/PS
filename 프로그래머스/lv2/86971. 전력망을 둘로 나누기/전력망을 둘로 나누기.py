from collections import deque, defaultdict
import sys

class Electricity:
    def __init__(self, N: int, wires: list) -> None:
        self.wires: list[list[int]] = wires
        self.N = N
        self.net: defaultdict[int, set[int]] = defaultdict(set)
        for u, v in self.wires:
            self.net[u].add(v)
            self.net[v].add(u)
    
    def divide(self) -> int:
        answer = sys.maxsize
        for edge in self.wires:
            u, v = edge
            self.net[u].discard(v)
            self.net[v].discard(u)
            answer = min(answer, abs(self.find_connected(u) - self.find_connected(v)))
            self.net[u].add(v)
            self.net[v].add(u)
        return answer
            
    
    def find_connected(self, start: int) -> int:
        Q: deque[int] = deque([start])
        checked: set[int] = set()
        while Q:
            u = Q.popleft()
            if u in checked:
                continue
            checked.add(u)
            Q.extend(self.net[u])
        return len(checked)
            

def solution(N, wires):
    elec = Electricity(N, wires)
    return elec.divide()