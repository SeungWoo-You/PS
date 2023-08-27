def main():
    N = input()
    length = len(N)
    num = 1
    seq = ''

    while len(seq) < length:
        seq += str(num)
        num += 1

    i = 0
    while True:
        if i + length >= len(seq):
            seq += str(num)
            num += 1
            continue
        if seq[i: i + length] == N:
            break
        i += 1
    print(i + 1)


if __name__ == '__main__':
    main()
