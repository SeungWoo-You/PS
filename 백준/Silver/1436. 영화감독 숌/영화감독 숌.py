def main():
    N = int(input())
    count = 0
    num = 0
    while count < N:
        num += 1
        if '666' in str(num):
            count += 1
    print(num)


if __name__ == '__main__':
    main()
