import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

V, E = map(int, input().split())
parents: list[int] = [i for i in range(V + 1)]

graph: list[tuple[int, int, int]] = []
for _ in range(E):
    u, v, w = map(int, input().split())
    graph.append((u, v, w));

graph.sort(key=lambda x: x[2]);

def find(x: int) -> int:
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]

def union(a: int, b: int) -> None:
    a = find(a)
    b = find(b)
    
    if a < b:
        parents[b] = a
    else:
        parents[a] = b

answer: int = 0
for a, b, c in graph:
    if find(a) != find(b):
        union(a, b)
        answer += c

print(answer)
