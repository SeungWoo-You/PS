def main():
    T = int(input())
    for _ in range(T):
        ans = input()
        total = 0
        count = 0
        for char in ans:
            if char == 'O':
                count += 1
            else:
                total += count * (count + 1) // 2
                count = 0
        total += count * (count + 1) // 2
        print(total)


if __name__ == '__main__':
    main()
