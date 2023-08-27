import sys


class Node:
    def __init__(self, value: str) -> None:
        self.value = value
        self.children: dict[str, Node] = dict()


def main():
    N = int(input())
    colony = Node('-1')
    for _ in range(N):
        data = input().strip().split()
        K = int(data[0])
        temp = colony
        for x in data[1:]:
            if x in temp.children:
                temp = temp.children[x]
                continue
            temp.children[x] = Node(x)
            temp = temp.children[x]
    print_colony(colony, -1)


def print_colony(room: Node, rank: int) -> None:
    if room.value != '-1':
        print('--' * rank, room.value, sep='')
    for _, r in sorted(room.children.items()):
        print_colony(r, rank + 1)


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
