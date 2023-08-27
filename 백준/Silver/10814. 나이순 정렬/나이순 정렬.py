from collections import defaultdict


def main():
    N = int(input())
    D: defaultdict[int, list[str]] = defaultdict(list)
    for _ in range(N):
        age, name = input().split()
        age = int(age)
        D[age].append(name)
    for k in sorted(D.keys()):
        for n in D[k]:
            print(k, n)


if __name__ == '__main__':
    main()
