def solution(n):
    tower = [[0] * n for _ in range(n)]
    x, y = 0, 0
    tower[x][y] = 1
    way = 0
    i = 2
    N = n * (n + 1) // 2
    while i <= N:
        if way == 0:
            x += 1
            if x >= n or tower[x][y] != 0:
                x -= 1
                way = 1
        if way == 1:
            y += 1
            if y >= n or tower[x][y] != 0:
                y -= 1
                way = 2
        if way == 2:
            x -= 1
            y -= 1
            if x < 0 or y < 0 or tower[x][y] != 0:
                x += 1
                y += 1
                way = 0
                continue
        tower[x][y] = i
        i += 1
    answer = []
    for row in tower:
        answer.extend([x for x in row if x != 0])
    return answer