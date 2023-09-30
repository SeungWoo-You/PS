import sys

def main():
    A, B, C = map(int, input().split())
    print(*[(A + B) % C for _ in range(2)], sep='\n')
    print(*[(A * B) % C for _ in range(2)], sep='\n')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()