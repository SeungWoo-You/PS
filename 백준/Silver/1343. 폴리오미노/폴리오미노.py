import sys


def main():
    boards = input().strip().split('.')
    res: list[str] = []
    for B in boards:
        temp = ''
        p1, rem = divmod(len(B), 4)
        temp += p1 * 'AAAA'
        p2, R = divmod(rem, 2)
        if R != 0:
            print(-1)
            return
        temp += p2 * 'BB'
        res.append(temp)
    print('.'.join(res))


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
