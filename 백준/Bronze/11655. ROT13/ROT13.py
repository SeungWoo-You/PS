import sys


def main():
    S = input().rstrip('\n')

    res = ''
    for x in S:
        if x.isdigit() or x == ' ':
            res += x
            continue
        if x.isupper():
            x = chr((ord(x) - ord('A') + 13) % 26 + ord('A'))
        elif x.islower():
            x = chr((ord(x) - ord('a') + 13) % 26 + ord('a'))
        res += x
    print(res)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
