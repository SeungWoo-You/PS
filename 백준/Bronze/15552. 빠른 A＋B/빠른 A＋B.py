import sys

def main():
    T = int(input())
    for _ in range(T):
        A, B = map(int, input().split())
        print(A + B)
        
        
if __name__ == '__main__':
    input = sys.stdin.readline
    main()