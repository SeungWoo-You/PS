import math

def main():
    A, B = map(int, input().split())
    print(math.gcd(A, B))
    print(math.lcm(A, B))


if __name__ == '__main__':
    main()