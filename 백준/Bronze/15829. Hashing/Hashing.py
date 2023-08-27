def main():
    r = 31
    M = 1234567891
    L = input()
    line = input()
    res = 0
    for i, x in enumerate(line):
        a = ord(x) - ord('a') + 1
        res = (res + a * r**i) % M
    print(res)


if __name__ == '__main__':
    main()
