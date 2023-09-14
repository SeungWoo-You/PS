from collections import defaultdict, deque

class Graph:
    def __init__(self, N: int, edges: list):
        self.N: int = N
        self.edges: list[list[int]] = edges
        self.nodes: defaultdict[int, set[int]] = defaultdict(set)
        self.make()
        
    def make(self) -> None:
        for E in self.edges:
            u, v = E
            self.nodes[u].add(v)
            self.nodes[v].add(u)
            
    def BFS(self) -> int:
        visited: list[int] = [-1] * (self.N + 1)
        dist = 0
        Q: deque[tuple[int, int]] = deque([(1, dist)])
        while Q:
            u, d = Q.popleft()
            if visited[u] != -1:
                continue
            visited[u] = d
            dist = max(dist, d)
            Q.extend([(v, d + 1) for v in self.nodes[u]])
        
        answer = 0
        for d in visited:
            if d == dist:
                answer += 1
        return answer

def solution(n, edges):
    answer = 0
    graph = Graph(n, edges)
    return graph.BFS()