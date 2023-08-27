import sys


class Node:
    def __init__(self, root: str) -> None:
        self.root = root
        self.children: dict[str, Node] = dict()
        self.value = 0


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        tree = Node('-1')
        call_list = [input().strip() for _ in range(n)]

        try:
            for call in call_list:
                temp = tree
                check = True
                for j, c in enumerate(call):
                    if c in temp.children.keys():
                        temp = temp.children[c]
                        if temp.value == 1:
                            raise Exception
                    else:
                        temp.children[c] = Node(c)
                        temp = temp.children[c]
                        if j == len(call) - 1:
                            temp.value = 1
                            check = False
                if check:
                    raise Exception
            print('YES')
        except:
            print('NO')


if __name__ == '__main__':
    input = sys.stdin.readline
    main()
