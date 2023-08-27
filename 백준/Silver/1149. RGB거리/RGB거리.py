def main():
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    print(min_cost(costs))


def min_cost(costs: list[list[int, int, int]]) -> int:
    R = G = B = 0
    for c in costs:
        r, g, b = c
        R, G, B = min(G + r, B + r), min(R + g, B + g), min(R + b, G + b)
    return min(R, G, B)


if __name__ == '__main__':
    main()
