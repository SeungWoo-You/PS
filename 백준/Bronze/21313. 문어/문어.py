def main():
    N = int(input())
    quot, rem = divmod(N, 2)
    if rem == 0:
        print('1 2 ' * quot)
    else:
        print('1 2 ' * quot + '3')


if __name__ == '__main__':
    main()
