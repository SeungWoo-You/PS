from collections import deque


class Maze:
    def __init__(self, maps: list) -> None:
        self.N = len(maps)
        self.M = len(maps[0])
        self.maps: list[str] = maps
        for i, row in enumerate(self.maps):
            for j, x in enumerate(row):
                if x == 'S':
                    self.pos = (i, j)
                    break
    
    def find(self, end: str) -> int:
        Q = deque([(*self.pos, 0)])
        Dx = [0, 0, 1, -1]
        Dy = [1, -1, 0, 0]
        checked: set[tuple[int, int]] = set()
        while Q:
            i, j, d = Q.popleft()
            if self.maps[i][j] == end:
                self.pos = (i, j)
                return d
            if (i, j) in checked:
                continue
            checked.add((i, j))
            for dx, dy in zip(Dx, Dy):
                x, y = i + dx, j + dy
                if 0 <= x < self.N and 0 <= y < self.M and self.maps[x][y] != 'X':
                    Q.append((x, y, d + 1))
        return -1
            
        

def solution(maps):
    maps: list[str]
    answer = 0
    maze = Maze(maps)
    count = maze.find('L')
    if count == -1:
        return -1
    answer += count
    count = maze.find('E')
    if count == -1:
        return -1
    answer += count
    return answer