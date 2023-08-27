def main():
    L, C = map(int, input().split())
    chars = input().split()
    chars.sort()
    res = []
    temp = ''
    find_pw(L, C, chars, 0, temp, res)
    print(*res, sep='\n')


def find_pw(L: int, C: int, chars: list[str], n: int, temp: str, res: list[str]) -> None:
    if len(temp) == L:
        vowel = {'a', 'e', 'i', 'o', 'u'}
        temp_set = set(temp)
        if len(vowel.intersection(temp_set)) >= 1 and len(temp_set - vowel) >= 2:
            res.append(temp)
        return

    for i in range(n, C):
        temp += chars[i]
        find_pw(L, C, chars, i + 1, temp, res)
        temp = temp[:-1]


if __name__ == '__main__':
    main()
