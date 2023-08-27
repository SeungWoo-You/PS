def main():
    line = input()
    while line != '#':
        count = 0
        for char in line:
            if char.lower() in ['a', 'e', 'i', 'o', 'u']:
                count += 1
        print(count)
        line = input()


if __name__ == '__main__':
    main()
