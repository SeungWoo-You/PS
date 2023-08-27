def main():
    A, B = map(int, input().split())
    partial = partial_sum(B)
    print(partial[B - 1] - partial[A - 2]) if A != 1 else print(partial[B - 1])


def partial_sum(B: int) -> list[int]:
    partial = [1]

    N_max = 45
    for n in range(2, N_max + 1):
        for _ in range(n):
            if len(partial) == B:
                break
            partial.append(n + partial[-1])
    return partial


if __name__ == '__main__':
    main()
