def main():
    A, B, C = map(int, input().split())
    while (A, B, C) != (0, 0, 0):
        A, B, C = sorted([A, B, C])
        if A**2 + B**2 == C**2:
            print('right')
        else:
            print('wrong')
        A, B, C = map(int, input().split())


if __name__ == '__main__':
    main()
