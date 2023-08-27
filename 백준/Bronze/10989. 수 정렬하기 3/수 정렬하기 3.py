import sys

def main():
    input = sys.stdin.readline
    N = int(input())
    counter = [0] * 10001
    for _ in range(N):
        counter[int(input())] += 1

    for i in range(1, 10001):
        if counter[i] != 0:
            for _ in range(counter[i]):
                print(i)


if __name__ == '__main__':
    main()
