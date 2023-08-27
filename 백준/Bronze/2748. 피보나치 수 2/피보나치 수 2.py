import sys


def main():
    n = int(input())
    Fibo = [0, 1]
    while len(Fibo) < n + 1:
        Fibo.append(Fibo[-1] + Fibo[-2])
    print(Fibo[n])


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
