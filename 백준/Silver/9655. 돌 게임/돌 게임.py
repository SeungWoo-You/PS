import sys


def main():
    N = int(input())
    res = ['', 'SK', 'CY', 'SK']
    while len(res) <= N:
        if 'CY' in [res[-1], res[-3]]:
            res.append('SK')
        else:
            res.append('CY')
    print(res[N])


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
