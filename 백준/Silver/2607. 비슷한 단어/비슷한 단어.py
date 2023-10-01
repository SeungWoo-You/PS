import sys
from collections import Counter


def main():
    N = int(input())
    W = input().strip()
    W_count = Counter(W)
    w_list: list[Counter[str]] = []
    answer = 0
    for _ in range(1, N):
        S = input().strip()
        S_count = Counter(S)
        s_list: list[Counter[str]] = []
        if W_count == S_count:
            answer += 1
            continue
        for i in range(1, len(W) + 1):
            w_temp = Counter(W[:i - 1] + W[i:])
            w_list.append(w_temp)
            if w_temp == S_count:
                answer += 1
                break
        else:
            for i in range(1, len(S) + 1):
                s_temp = Counter(S[:i - 1] + S[i:])
                s_list.append(s_temp)
                if s_temp == W_count:
                    answer += 1
                    break
            else:
                for X in w_list:
                    for Y in s_list:
                        if X == Y:
                            answer += 1
                            break
                    else:
                        continue
                    break
    print(answer)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
