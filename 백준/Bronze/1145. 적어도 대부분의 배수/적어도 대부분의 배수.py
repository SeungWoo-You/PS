import itertools
import math


def main():
    five_numbers = list(map(int, input().split(" ")))
    combs = itertools.combinations(five_numbers, 3)
    res: list[int] = []
    for n1, n2, n3 in combs:
        almost_lcm = math.lcm(n1, n2, n3)
        res.append(almost_lcm)
    print(min(res))


if __name__ == '__main__':
    main()
