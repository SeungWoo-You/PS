import sys
from collections import defaultdict, deque


class Graph:
    def __init__(self) -> None:
        self.N: int
        self.M: int
        self.V: int
        self.graph: defaultdict[int, list[int]] = defaultdict(list)
        self.get_info()

    def get_info(self) -> None:
        self.N, self.M, self.V = map(int, input().split())
        for _ in range(self.M):
            u, v = map(int, input().split())
            self.graph[u].append(v)
            self.graph[v].append(u)

    def DFS(self) -> list[int]:
        stack = [self.V]
        ans: list[int] = []
        for value in self.graph.values():
            value.sort(reverse=True)
        checked: set[int] = set()
        while stack:
            u = stack.pop()
            if u in checked:
                continue
            ans.append(u)
            checked.add(u)
            stack.extend(self.graph[u])
        return ans

    def BFS(self) -> list[int]:
        Q = deque([self.V])
        ans: list[int] = []
        for value in self.graph.values():
            value.sort()
        checked: set[int] = set()
        while Q:
            u = Q.popleft()
            if u in checked:
                continue
            ans.append(u)
            checked.add(u)
            Q.extend(self.graph[u])
        return ans


def main():
    graph = Graph()
    print(*graph.DFS())
    print(*graph.BFS())


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
