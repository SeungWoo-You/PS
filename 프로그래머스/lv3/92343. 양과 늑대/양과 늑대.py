from copy import deepcopy

class Node:
    def __init__(self, idx, val, parent = None, left = None, right = None) -> None:
        self.idx: int = idx
        self.value: int = val
        self.parent: Node | None = parent
        self.left: Node | None = left
        self.right: Node | None = right

class Tree:
    def __init__(self, info: list, edges: list) -> None:
        self.info = info
        self.edges = edges
        self.root: Node
        self.make()
        self.answer = 0
        
    def make(self) -> None:
        nodes = [Node(i, self.info[i]) for i in range(len(self.info))]
        for E in self.edges:
            u, v = E
            if nodes[u].left == None:
                nodes[u].left = nodes[v]
            else:
                nodes[u].right = nodes[v]
        self.root = nodes[0]
    
    def collect(self, sheep: int, wolves: int, possible: set) -> None:
        if not possible:
            self.answer = max(self.answer, sheep)
            return
        if sheep <= wolves:
            return
        self.answer = max(self.answer, sheep)
        for T in possible:
            P = possible.copy()
            P.discard(T)
            if T.left != None:
                P.add(T.left)
            if T.right != None:
                P.add(T.right)
            if T.value == 0:
                self.collect(sheep + 1, wolves, P)
            if T.value == 1:
                self.collect(sheep, wolves + 1, P)
            

def solution(info, edges):
    tree = Tree(info, edges)
    P = set()
    if tree.root.left != None:
        P.add(tree.root.left)
    if tree.root.right != None:
        P.add(tree.root.right)
    tree.collect(1, 0, P)
    return tree.answer