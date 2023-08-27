import sys


def main():
    D = int(input())
    N, M, K = map(int, input().split())
    lim_n, rem_n = divmod(N, D)
    lim_m, rem_m = divmod(M, D)
    rem_n, rem_m = D - rem_n, D - rem_m

    temp = lim_m + lim_n
    cases = {(temp + K // D, K)}
    if rem_n != D:
        cases.add((temp + 1 + (K - rem_n) // D, K - rem_n))
    if rem_m != D:
        cases.add((temp + 1 + (K - rem_m) // D, K - rem_m))
    if rem_n != D and rem_m != D:
        cases.add((temp + 2 + (K - rem_n - rem_m) // D, K - rem_n - rem_m))
        
    t = 0
    res = 0
    for tot, rice in cases:
        if tot > t:
            res = rice
            t = tot
        elif tot == t:
            res = max(res, rice)
    print(res)


if __name__ == "__main__":
    input = sys.stdin.readline
    main()
