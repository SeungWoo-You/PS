import sys


def main():
    T = int(input())
    for _ in range(T):
        N = int(input())
        seq = list(map(int, input().split()))
        graph: dict[int, int] = {}
        for i, x in enumerate(seq, start=1):
            graph[i] = x
        print(count_chunk(graph, N))


def count_chunk(graph: dict[int, int], N: int) -> int:
    stack: list[int] = []
    checked: set[int] = set()
    node: set[int] = set([x for x in range(1, N + 1)])
    count = 0
    while len(checked) < N:
        count += 1
        s = node.pop()
        stack.append(s)
        while stack:
            v = stack.pop()
            if v in checked:
                continue
            checked.add(v)
            stack.append(graph[v])
        node -= checked
    return count


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
