import math


def main():
    N: int = int(input())
    numbers: list[int] = map(int, input().split(" "))

    count: int = 0
    for x in numbers:
        if is_prime(x) == True:
            count += 1
    print(count)


def is_prime(x: int) -> bool:
    if x == 1:
        return False
    for div in range(2, int(math.sqrt(x) + 1)):
        if x % div == 0:
            return False
    return True


if __name__ == '__main__':
    main()
