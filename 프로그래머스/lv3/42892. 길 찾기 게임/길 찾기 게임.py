import sys
sys.setrecursionlimit(10**5 + 10**4)


class Node:
    def __init__(self, idx: int, pos: list, parent, left, right) -> None:
        self.idx = idx
        self.parent: Node | None = parent
        self.pos = pos
        self.left: Node | None = left
        self.right: Node | None = right
        

class Tree:
    def __init__(self, nodeinfo: list) -> None:
        self.nodeinfo = list(zip(range(1, len(nodeinfo) + 1), nodeinfo))
        self.nodeinfo.sort(key=lambda p: -p[1][1])
        self.root = Node(*self.nodeinfo[0], None, None, None)
        L, R = [], []
        for T in self.nodeinfo:
            if T[1][0] < self.root.pos[0]:
                L.append(T)
            elif T[1][0] > self.root.pos[0]:
                R.append(T)
        self.make(L, R, self.root)
        
        
    def make(self, L: list, R: list, parent: Node) -> None:
        if not L and not R:
            return
        else:
            try:
                L.sort(key=lambda p: -p[1][1])
                node = Node(*L[0], parent, None, None)
                newL, newR = [], []
                for T in L:
                    if T[1][0] < node.pos[0]:
                        newL.append(T)
                    elif T[1][0] > node.pos[0]:
                        newR.append(T)
                parent.left = node
                self.make(newL, newR, node)
            except:
                pass
            try:
                R.sort(key=lambda p: -p[1][1])
                node = Node(*R[0], parent, None, None)
                newL, newR = [], []
                for T in R:
                    if T[1][0] < node.pos[0]:
                        newL.append(T)
                    elif T[1][0] > node.pos[0]:
                        newR.append(T)
                parent.right = node
                self.make(newL, newR, node)
            except:
                pass
            
    def preorder(self, answer: list, parent: Node) -> None:
        if parent == None:
            return
        else:
            answer.append(parent.idx)
            self.preorder(answer, parent.left)
            self.preorder(answer, parent.right)
            
    def postorder(self, answer: list, stack: list, parent: Node) -> None:
        if parent == None:
            return
        else:
            stack.append(parent.idx)
            self.postorder(answer, stack, parent.left)
            self.postorder(answer, stack, parent.right)
            answer.append(stack.pop())
            

def solution(nodeinfo):
    nodeinfo: list[list[int]]
    tree = Tree(nodeinfo)
    pre = []
    tree.preorder(pre, tree.root)
    post, stack = [], []
    tree.postorder(post, stack, tree.root)
    return [pre, post]