from collections import deque


def main():
    N = int(input())
    queue = deque(range(1, N + 1))
    while queue:
        rem = queue.popleft()
        try:
            queue.append(queue[0])
            queue.popleft()
        except:
            break
    print(rem)


if __name__ == '__main__':
    main()
