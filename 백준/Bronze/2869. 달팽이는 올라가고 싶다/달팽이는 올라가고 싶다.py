def main():
    A, B, V = map(int, input().split())
    quot, rem = divmod(V - A, A - B)
    print(quot + 1 if rem == 0 else quot + 2)


if __name__ == '__main__':
    main()
