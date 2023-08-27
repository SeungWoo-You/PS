from collections import Counter


def main():
    A = int(input())
    B = int(input())
    C = int(input())
    count = Counter(str(A * B * C))
    for i in range(10):
        try:
            print(count[str(i)])
        except:
            print(0)


if __name__ == '__main__':
    main()
