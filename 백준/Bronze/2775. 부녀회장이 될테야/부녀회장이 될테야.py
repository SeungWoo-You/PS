from collections import defaultdict


def main():
    T = int(input())
    people: defaultdict[int, list[int]] = defaultdict(list)
    people[0] = list(range(15))
    height = 0
    for _ in range(T):
        k = int(input())
        n = int(input())
        if k > height:
            for i in range(height + 1, k + 1):
                for j in range(15):
                    people[i].append(sum(people[i - 1][:j + 1]))
        print(people[k][n])


if __name__ == '__main__':
    main()
