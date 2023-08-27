def main():
    n = int(input())
    print(*stack(n), sep='\n')


def stack(n: int) -> list[str]:
    stack: list[int] = []
    res: list[str] = []

    i = 1
    cont = True
    for _ in range(n):
        num = int(input())
        if cont == False:
            continue
        if num >= i:
            for _ in range(num - i + 1):
                stack.append(i)
                i += 1
                res.append('+')
        if num == stack.pop():
            res.append('-')
        else:
            res = ['NO']
            cont = False
    return res


if __name__ == '__main__':
    main()
