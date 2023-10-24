import sys

def main():
    S = input().strip()
    answer = ''
    for c in S:
        if c.islower():
            answer += c.upper()
        else:
            answer += c.lower()
    print(answer)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
