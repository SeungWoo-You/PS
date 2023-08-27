def main():
    cost = int(input())
    pay = 1000
    print(count_change(pay, cost))


def count_change(pay: int, cost: int) -> int:
    count = 0
    changes = [500, 100, 50, 10, 5, 1]
    pay_back = pay - cost
    for m in changes:
        if pay_back == 0:
            break
        quot, rem = divmod(pay_back, m)
        pay_back = rem
        count += quot
    return count


if __name__ == '__main__':
    main()
