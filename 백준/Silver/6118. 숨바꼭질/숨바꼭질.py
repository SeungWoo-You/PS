from collections import defaultdict, deque


def main():
    global N
    N, M = map(int, input().split())
    places: defaultdict[int, set[int]] = defaultdict(set)
    for _ in range(M):
        v1, v2 = map(int, input().split())
        places[v1].add(v2)
        places[v2].add(v1)
    print(*hide_place(places))


def hide_place(place: defaultdict[int, set[int]]) -> tuple[int]:
    visited = [0 for _ in range(N + 1)]
    visited[0] = -1
    queue = deque([1])
    while queue:
        v = queue.popleft()
        for x in place[v]:
            if visited[x] == 0 and x != 1:
                queue.append(x)
                visited[x] = visited[v] + 1

    dist = max(visited)
    idx = count = 0
    for i, d in enumerate(visited):
        if d == dist:
            if count == 0:
                idx = i
            count += 1
    return idx, dist, count


if __name__ == '__main__':
    main()
