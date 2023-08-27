def main():
    T = int(input())
    for _ in range(T):
        num = input()
        if num.isdigit():
            res = num_to_roman(num)
        else:
            res = roman_to_num(num)
        print(res)


def roman_to_num(roman: str) -> int:
    roman_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    res: list[int] = []
    for x in roman:
        n = roman_dict[x]
        if not res:
            pass
        elif res[-1] < n:
            n = n - res[-1]
            res[-1] = n
            continue
        res.append(n)
    return sum(res)


def num_to_roman(num: str) -> str:
    num_dict = {
        1: 'I',
        5: 'V',
        10: 'X',
        50: 'L',
        100: 'C',
        500: 'D',
        1000: 'M'
    }
    res: str = ''
    digit = len(num)
    for i, _x in enumerate(num):
        x = int(_x)
        if x >= 5:
            x -= 5
            only_1 = [1 for _ in range(x)]
            if len(only_1) == 4:
                decompos = [1, 10]
            else:
                decompos = [5] + only_1
        else:
            only_1 = [1 for _ in range(x)]
            if len(only_1) == 4:
                decompos = [1, 5]
            else:
                decompos = only_1
        for d in decompos:
            n = num_dict[d * (10 ** (digit - i - 1))]
            res += n
    return res


if __name__ == '__main__':
    main()
