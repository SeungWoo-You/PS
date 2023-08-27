from collections import Counter


def main():
    T = 3
    ans = ['E', 'A', 'B', 'C', 'D']
    for _ in range(T):
        state = Counter(map(int, input().split()))
        print(ans[state[0]])


if __name__ == '__main__':
    main()
