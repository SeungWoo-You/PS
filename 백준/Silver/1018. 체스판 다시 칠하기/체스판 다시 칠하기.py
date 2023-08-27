from collections import Counter


def main():
    M, N = map(int, input().split())
    board = [list(input()) for _ in range(M)]
    print(count_color(board, M, N))


def count_color(board: list[list[str]], M: int, N: int) -> int:
    count = float('inf')
    for i in range(M - 7):
        for j in range(N - 7):
            count_1, count_2 = 0, 0
            for p in range(8):
                for q in range(8):
                    if (p + q) % 2 == 0:
                        if board[i + p][j + q] != 'B':
                            count_1 += 1
                        else:
                            count_2 += 1
                    if (p + q) % 2 == 1:
                        if board[i + p][j + q] == 'B':
                            count_1 += 1
                        else:
                            count_2 += 1
            count = min(count, count_1, count_2)
    return count


if __name__ == '__main__':
    main()
