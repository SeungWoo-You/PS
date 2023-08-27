from collections import Counter


def main():
    word = input().upper()
    count = Counter(word)
    res: set[str] = set()
    num = 0
    for k, v in count.items():
        if v > num:
            res.clear()
            res.add(k)
            num = v
        elif v == num:
            res.add(k)
    print(*res) if len(res) == 1 else print("?")


if __name__ == '__main__':
    main()
