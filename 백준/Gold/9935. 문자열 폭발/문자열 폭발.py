def main():
    line = input()
    bomb = input()
    b_len = len(bomb)
    check: list[str] = []
    i = 0
    N = len(line)

    while i < N:
        if len(check) < b_len or ''.join(check[-b_len:]) != bomb:
            check.append(line[i])
            i += 1
        else:
            for _ in bomb:
                check.pop()
    while ''.join(check[-b_len:]) == bomb:
        for _ in bomb:
            check.pop()
    print(''.join(check) if check else 'FRULA')


if __name__ == '__main__':
    main()
