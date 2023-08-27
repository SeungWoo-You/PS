def main():
    res = set()
    for _ in range(10):
        x = int(input())
        rem = x % 42
        res.add(rem)
    print(len(res))


if __name__ == '__main__':
    main()
