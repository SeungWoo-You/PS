def main():
    S = input()
    res = [-1] * 26
    for pos, char in enumerate(S):
        idx = ord(char) - ord('a')
        if res[idx] == -1:
            res[idx] = pos
    print(*res)


if __name__ == '__main__':
    main()
