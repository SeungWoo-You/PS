def main():
    num = input()
    while num != '0':
        print('yes') if num == ''.join(reversed(num)) else print('no')
        num = input()


if __name__ == '__main__':
    main()
