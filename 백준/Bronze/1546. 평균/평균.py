def main():
    N = int(input())
    scores = list(map(int, input().split()))
    M = max(scores)
    print(sum(scores) / M * 100 / N)


if __name__ == '__main__':
    main()
