import sys


def main():
    n = int(input())
    mat = calc_mat_power([[1, 1], [1, 0]], n - 1)
    print(mat[0][0])


def calc_mat_power(M: list[list[int]], n: int) -> list[list[int]]:
    if n == 0:
        return [[1, 0], [0, 1]]
    elif n == 1:
        return M
    elif n == 2:
        return product_mat(M, M)
    else:
        if n % 2 == 1:
            temp = calc_mat_power(M, (n - 1) // 2)
            temp = product_mat(temp, temp)
            return product_mat(temp, M)
        else:
            temp = calc_mat_power(M, n // 2)
            return product_mat(temp, temp)


def product_mat(M1: list[list[int]], M2: list[list[int]]) -> list[list[int]]:
    a1 = M1[0][0] * M2[0][0] + M1[0][1] * M2[1][0]
    a2 = M1[0][0] * M2[0][1] + M1[0][1] * M2[1][1]
    a3 = M1[1][0] * M2[0][0] + M1[1][1] * M2[1][0]
    a4 = M1[1][0] * M2[0][1] + M1[1][1] * M2[1][1]
    return [[a1, a2], [a3, a4]]


if __name__ == "__main__":
    input = sys.stdin.readline
    sys.setrecursionlimit(10**5)
    main()
