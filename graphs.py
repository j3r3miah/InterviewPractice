from collections import deque


class Graph:
    nodes = []

    def reset(self):
        for n in self.nodes:
            n.reset()


class Node:
    value = None
    children = []

    visited = False
    marked = False
    parent = None

    def __init__(self, value):
        self.value = value

    def reset(self):
        self.visited = self.marked = False
        self.parent = None

    def __repr__(self):
        return str(self.value)


def find_path_dfs(g, s, e):
    if g:
        g.reset()
    s.visited = True
    if s == e:
        return [e]
    for n in s.children:
        if not n.visited:
            rv = find_path_dfs(None, n, e)
            if rv:
                rv.insert(0, s)
                return rv
    return None


def find_path(g, s, e):  # BFS, shortest path
    g.reset()
    q = deque([s])
    s.marked = True
    while len(q):
        n = q.popleft()
        if n == e:
            rv = [e]
            p = e.parent
            while p:
                rv.append(p)
                p = p.parent
            return rv[::-1]
        for c in n.children:
            if not c.marked:
                c.parent = n
                c.marked = True
                q.append(c)
    return None


if __name__ == '__main__':
    g = Graph()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n5 = Node(5)
    n7 = Node(7)
    g.nodes = [n1, n2, n3, n5, n7]
    n1.children = [n2, n7]
    n2.children = [n1, n5]
    n3.children = []
    n5.children = [n7]
    n7.children = []

    print(find_path(g, n1, n7))
    print(find_path(g, n1, n5))
    print(find_path(g, n1, n3))
    print(find_path(g, n2, n7))
    print(find_path(g, n2, n1))
    print(find_path(g, n2, n5))
    print(find_path(g, n2, n2))
