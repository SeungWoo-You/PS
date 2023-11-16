import sys


def main():
    M, N = map(int, input().split())
    trans_table = {
        0: 'zero',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine'
    }
    answer: dict[str, int] = {}
    for num in range(M, N + 1):
        eng = ''
        for i in str(num):
            eng += trans_table[int(i)]
        answer[eng] = num
    count = 0
    for _, v in sorted(answer.items()):
        if count == 10:
            print()
            count = 0
        print(v, end=' ')
        count += 1


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
