def main():
    T = int(input())
    for _ in range(T):
        line = list(input())
        check: list[str] = []
        valid = True
        for x in line:
            if x == '(':
                check.append(x)
            if x == ')':
                try:
                    check.pop()
                except:
                    valid = False
                    break
        if check or valid == False:
            print('NO')
        else:
            print('YES')


if __name__ == '__main__':
    main()
