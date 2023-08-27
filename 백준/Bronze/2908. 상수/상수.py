def main():
    A, B = map(int, map(''.join, map(reversed, input().split())))
    print(A) if A > B else print(B)


if __name__ == '__main__':
    main()
