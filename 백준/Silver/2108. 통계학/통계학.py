from collections import Counter


def main():
    N = int(input())
    ls = [int(input()) for _ in range(N)]
    ls.sort()

    median = ls[N // 2]
    counter = Counter(ls)
    freq: list[int] = []
    M = -float('inf')
    r = 0
    m = float('inf')
    geo_sum = 0
    for x, rank in counter.items():
        if rank > r:
            freq.clear()
            freq.append(x)
            r = rank
        elif rank == r:
            freq.append(x)
        if x > M:
            M = x
        if x < m:
            m = x
        geo_sum += x * rank
    geo_mean = geo_sum / N

    print(int(round(geo_mean, 0)))
    print(median)
    print(freq[0] if len(freq) == 1 else freq[1])
    print(M - m)


if __name__ == '__main__':
    main()
