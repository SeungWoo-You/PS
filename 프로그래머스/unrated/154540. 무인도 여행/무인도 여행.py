class Tour:
    def __init__(self, maps: list) -> None:
        self.maps: list[str] = maps
        self.land: set[tuple[int, int]] = set()
        for i, row in enumerate(self.maps):
            for j, x in enumerate(row):
                try:
                    _ = int(x)
                    self.land.add((i, j))
                except:
                    pass
    
    def rest(self) -> list:
        answer: list[int] = []
        Dx = [0, 0, -1, 1]
        Dy = [-1, 1, 0, 0]
        while self.land:
            src = list(self.land)[0]
            i, j = src
            count = 0
            stack: list[tuple[int, int, int]] = [(i, j)]
            while stack:
                i, j = stack.pop()
                if (i, j) not in self.land:
                    continue
                self.land.discard((i, j))
                count += int(self.maps[i][j])
                for dx, dy in zip(Dx, Dy):
                    x, y = i + dx, j + dy
                    if 0 <= x < len(self.maps) and 0 <= y < len(self.maps[0]) and self.maps[x][y] != 'X':
                        stack.append((x, y))
            answer.append(count)
        answer.sort()
        return answer if answer else [-1]

def solution(maps):
    tour = Tour(maps)
    return tour.rest()