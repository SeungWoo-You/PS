import sys


def main():
    N, K = map(int, input().split())
    table = list(input().strip())
    count = 0
    for i in range(N):
        if table[i] == 'P':
            for j in range(max(i - K, 0), i):
                if table[j] == 'H':
                    table[j] = 'N'
                    count += 1
                    break
            else:
                for j in range(i + 1, min(i + K + 1, N)):
                    if table[j] == 'H':
                        table[j] = 'N'
                        count += 1
                        break
    print(count)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
