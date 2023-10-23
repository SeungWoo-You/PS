import sys
from itertools import permutations


def main():
    K = int(input())
    signs = input().strip().split()
    m, M = '', ''
    for T in permutations(range(10), K + 1):
        prev = T[0]
        for i in range(1, K + 1):
            if signs[i - 1] == '>' and prev > T[i]:
                prev = T[i]
                continue
            elif signs[i - 1] == '<' and prev < T[i]:
                prev = T[i]
                continue
            break
        else:
            S = ''.join(map(str, T))
            if not m:
                m = M = S
            else:
                if int(M) < int(S):
                    M = S
                if int(m) > int(S):
                    m = S
    print(M, m, sep='\n')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
