def main():
    while True:
        A, B = map(int, input().split())
        if (A, B) == (0, 0):
            break
        print(A + B)


if __name__ == '__main__':
    main()
