from collections import deque


def main():
    n, w, L = map(int, input().split())
    trucks = deque(map(int, input().split()))
    print(truck_times(n, w, L, trucks))


def truck_times(n: int, w: int, L: int, trucks: deque[int]) -> int:
    count = 0
    queue: deque[tuple[int, int]] = deque([])
    weight = 0
    movable = True

    while trucks:
        count += 1
        if queue and count - queue[0][1] >= w:
            trs = queue.popleft()
            weight -= trs[0]
            movable = True
        if movable and L < weight + trucks[0]:
            movable = False
        elif movable and L >= weight + trucks[0]:
            tr = trucks.popleft()
            queue.append((tr, count))
            weight += tr

    return count + w


if __name__ == '__main__':
    main()
