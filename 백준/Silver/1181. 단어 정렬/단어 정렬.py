def main():
    N = int(input())
    words = {input() for _ in range(N)}
    res = sorted(words, key=lambda w: (len(w), w))
    print(*res, sep='\n')


if __name__ == '__main__':
    main()
