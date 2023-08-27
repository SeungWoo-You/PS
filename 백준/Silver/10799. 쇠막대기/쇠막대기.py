import sys


def main():
    bars = list(input().strip())
    prev = bars[0]
    stack: list[str] = []
    count = 0
    for b in bars:
        if prev == '(' and b == ')':
            stack.pop()
            count += len(stack)
        elif b == ')':
            stack.pop()
            count += 1
        else:
            stack.append(b)
        prev = b
    print(count)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
