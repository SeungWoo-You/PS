import math


def main():
    N = int(input())
    A_ls = list(map(int, input().split()))
    opers = list(map(int, input().split()))
    Mm = [-math.inf, math.inf]
    res = A_ls[0]
    find_values(A_ls, 1, opers, res, Mm)
    print(*Mm, sep='\n')


def find_values(A: list[int], i: int, opers: list[int], res: int, Mm: list[int]) -> None:
    if i == len(A):
        Mm[0] = max(Mm[0], res)
        Mm[1] = min(Mm[1], res)
        return

    if opers[0] > 0:
        opers[0] -= 1
        find_values(A, i + 1, opers, res + A[i], Mm)
        opers[0] += 1
    if opers[1] > 0:
        opers[1] -= 1
        find_values(A, i + 1, opers, res - A[i], Mm)
        opers[1] += 1
    if opers[2] > 0:
        opers[2] -= 1
        find_values(A, i + 1, opers, res * A[i], Mm)
        opers[2] += 1
    if opers[3] > 0:
        opers[3] -= 1
        find_values(A, i + 1, opers, int(res / A[i]), Mm)
        opers[3] += 1


if __name__ == '__main__':
    main()
