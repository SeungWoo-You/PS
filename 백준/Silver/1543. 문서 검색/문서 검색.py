import sys


def main():
    S = input().rstrip('\n')
    word = input().rstrip('\n')
    l = len(word)

    end = 0
    count = 0
    while end + l - 1 <= len(S):
        if S[end:end + l] == word:
            count += 1
            end += l
        else:
            end += 1
    print(count)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
