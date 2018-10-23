class Node:
    data = None
    left = None
    right = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return str(self.data)


class BST:
    root = None

    def insert(self, data):
        def _insert(root, new_node):
            if not root:
                return new_node
            if new_node.data < root.data:
                root.left = _insert(root.left, new_node)
            else:
                root.right = _insert(root.right, new_node)
            return root

        self.root = _insert(self.root, Node(data))

    def bfs(self):
        from collections import deque
        q = deque([self.root])
        while q:
            node = q.popleft()
            if node:
                print(node.data)
                q.append(node.left)
                q.append(node.right)

    def levels(self):
        rv = []
        found = False
        if self.root:
            rv.append([self.root])
            found = True
        while found:
            found = False
            next_level = []
            for n in rv[-1]:
                if n:
                    next_level.append(n.left)
                    next_level.append(n.right)
                    if n.left or n.right:
                        found = True
                else:
                    next_level.extend([None, None])
            if found:
                rv.append(next_level)
        return rv

    def __repr__(self):
        lines = []
        levels = self.levels()
        max_nodes = 2**(len(levels) - 1)
        item_width = 5
        space = ' '

        for d, level in enumerate(levels):
            line1 = []
            line2 = []
            num_nodes = 2**d
            margin_width = int(
                (max_nodes - num_nodes + 1) * item_width / (num_nodes + 1)
            )
            print(margin_width)
            line1.append(space * margin_width)
            line2.append(space * margin_width)
            for i, n in enumerate(level):
                if n:
                    if i % 2 == 0:
                        connector = '/'.rjust(item_width)
                    else:
                        connector = '\\'.ljust(item_width)
                    line1.append(connector)
                    line2.append(str(n.data).center(item_width))
                else:
                    line1.append(space * item_width)
                    line2.append(space * item_width)
                line1.append(space * margin_width)
                line2.append(space * margin_width)
            if d > 0:
                lines.append(''.join(line1))
            lines.append(''.join(line2))
        return '\n'.join(lines)


if __name__ == '__main__':
    from random import randint

    tree = BST()
    for i in range(0, 10):
        tree.insert(randint(0, 99))
    # tree.root = Node(5)
    # node = tree.root
    # node.left = Node(2)
    # node.right = Node(8)
    # node = tree.root.left
    # node.left = Node(1)
    # node.right = Node(3)
    # node = tree.root.right
    # node.left = Node(7)
    # node.right = Node(9)

    # tree.bfs()
    print(tree.levels())
    print(tree)
