import sys


def main():
    R, C = map(int, input().split())
    board = [list(input().strip()) for _ in range(R)]
    print(find_route(board, R, C))


def find_route(board: list[list[str]], R: int, C: int) -> int:
    queue = {(0, 0, board[0][0])}

    Dx = [-1, 1, 0, 0]
    Dy = [0, 0, -1, 1]

    ans = 1
    while queue:
        i, j, checked = queue.pop()
        for dx, dy in zip(Dx, Dy):
            x = i + dx
            y = j + dy
            if 0 <= x < R and 0 <= y < C and board[x][y] not in checked:
                queue.add((x, y, checked + board[x][y]))
                ans = max(ans, len(checked) + 1)
    return ans


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
