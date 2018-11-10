import pytest


class Node:
    data = None
    left = None
    right = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f'Node<{self.data}>'


class BST:
    root = None

    def __init__(self, items=None):
        if items:
            for o in items:
                self.insert(o)

    def insert(self, data):
        def _insert(root, node):
            if root is None:
                return node
            if node.data < root.data:
                root.left = _insert(root.left, node)
            elif node.data > root.data:
                root.right = _insert(root.right, node)
            # if node is a duplicate, it is not inserted
            return root
        self.root = _insert(self.root, Node(data))

    def search(self, data):
        cur = self.root
        while cur is not None:
            if cur.data == data:
                return True
            elif data < cur.data:
                cur = cur.left
            else:
                cur = cur.right
        return False

    def delete(self, data):
        def _min_node(root):
            while root.left:
                root = root.left
            return root

        def _delete(root, data):
            if root is None:
                return root
            if data < root.data:
                root.left = _delete(root.left, data)
            elif data > root.data:
                root.right = _delete(root.right, data)
            else: # we found the node to delete
                # only one child, just jump over the node to delete
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left
                # node to delete has two children. replace node with in-order
                # successor and delete successor.
                successor = _min_node(root.right)
                root.data = successor.data
                root.right = _delete(root.right, successor.data)
            return root

        self.root = _delete(self.root, data)

    def validate(self):
        def _validate(root):
            if root is None:
                return True
            if root.left and root.left.data >= root.data:
                return False
            if root.right and root.right.data <= root.data:
                return False
            return _validate(root.left) and _validate(root.right)
        return _validate(self.root)

    def rebalance(self):
        def _traverse(root, nodes):
            if root is None:
                return
            _traverse(root.left, nodes)
            nodes.append(root)
            _traverse(root.right, nodes)

        def _rebalance(nodes, low, high):
            if low > high:
                return None
            mid = (low + high) // 2
            root = nodes[mid]
            root.left = _rebalance(nodes, low, mid-1)
            root.right = _rebalance(nodes, mid+1, high)
            return root

        nodes = []
        _traverse(self.root, nodes)
        self.root = _rebalance(nodes, 0, len(nodes)-1)

    def traverse_in_order(self):
        rv = []
        def _traverse(root):
            if root is None:
                return
            _traverse(root.left)
            rv.append(root.data)
            _traverse(root.right)
        _traverse(self.root)
        return rv

    def traverse_level_order(self):
        rv = []
        level = [self.root]
        while any(level):
            rv.append(level)
            level = []
            for node in rv[-1]:
                if node is None:
                    continue
                level.append(node.left)
                level.append(node.right)
        return [[n.data if n else None for n in level] for level in rv]

    def traverse_paths(self):
        def _dfs(root, path, rv):
            if root is None:
                return
            path.append(root.data)
            if root.left is None and root.right is None:
                rv.append(path[:])
            else:
                if root.left:
                    _dfs(root.left, path, rv)
                if root.right:
                    _dfs(root.right, path, rv)
            path.pop()
        rv = []
        _dfs(self.root, [], rv)
        return rv

    def has_path_sum(self, value):
        def _has_path_sum(root, value):
            if root is None:
                return value == 0
            return (
                _has_path_sum(root.left, value - root.data) or
                _has_path_sum(root.right, value - root.data)
            )
        return _has_path_sum(self.root, value)

    @property
    def minimum(self):
        if self.root is None:
            return None
        cur = self.root
        while cur.left:
            cur = cur.left
        return cur.data

    @property
    def maximum(self):
        if self.root is None:
            return None
        cur = self.root
        while cur.right:
            cur = cur.right
        return cur.data

    @property
    def depth(self):
        def _depth(root):
            if root is None:
                return 0
            return 1 + max(_depth(root.left), _depth(root.right))
        return _depth(self.root)

    def __len__(self):
        def _count(root):
            if root is None:
                return 0
            return 1 + _count(root.left) + _count(root.right)
        return _count(self.root)

    def __eq__(self, other):
        if self is other:
            return True
        def _equals(root1, root2):
            if root1 is None or root2 is None:
                return root1 == root2
            if root1.data != root2.data:
                return False
            return (
                _equals(root1.left, root2.left) and
                _equals(root1.right, root2.right)
            )
        return _equals(self.root, other.root)

    @classmethod
    def from_preorder(cls, preorder):
        def make_tree(items):
            if not items:
                return None
            node = Node(items[0])
            if len(items) > 1:
                for i, v in enumerate(items):
                    if v > node.data:
                        break
                node.left = make_tree(items[1:i])
                node.right = make_tree(items[i:])
            return node

        tree = cls()
        tree.root = make_tree(preorder)
        return tree


class TestBST:
    def test_insert(self):
        tree = BST([5, 9, 7, 3, 2])
        assert(tree.root.data == 5)
        assert(tree.root.right.data == 9)
        assert(tree.root.right.left.data == 7)
        assert(tree.root.left.data == 3)
        assert(tree.root.left.left.data == 2)

    def test_search(self):
        items = [5, 9, 7, 3, 2]
        tree = BST(items)
        for o in items:
            assert(tree.search(o))
            assert(tree.search(o * 10) == False)

    def test_delete(self):
        tree = BST([5, 9, 7, 3, 2])
        tree.delete(5)
        assert(tree.search(5) == False)
        remaining = [7, 2, 9, 3]
        for o in remaining:
            assert(tree.search(o))
        for o in remaining:
            tree.delete(o)
        assert(tree.root is None)

    def test_minmax(self):
        tree = BST([5, 9, 7, 3, 2])
        assert(tree.minimum == 2)
        assert(tree.maximum == 9)
        assert(BST().minimum is None)
        assert(BST().maximum is None)

    def test_depth(self):
        assert(BST().depth == 0)
        assert(BST([4]).depth == 1)
        assert(BST([3, 2]).depth == 2)
        assert(BST([5, 9, 7, 3, 2]).depth == 3)

    def test_len(self):
        assert(len(BST([5, 9, 7, 3, 2])) == 5)
        assert(len(BST([3, 2])) == 2)

    def test_equals(self):
        tree = BST([5, 9, 7, 3, 2])
        assert(tree == tree)
        assert(tree == BST([5, 9, 7, 3, 2]))
        assert(not(tree == BST([5, 9, 7, 3, 2, 8])))
        assert(not(tree == BST([2, 3, 7, 9, 5])))
        assert(not(tree == BST()))

    def test_validate(self):
        tree = BST([5, 9, 7, 3, 2])
        assert(tree.validate())
        tree.root.data = 10
        assert(tree.validate() is False)
        tree = BST(['g', 'b', 'd', 'h', 't', 'z', 'a'])
        assert(tree.validate())

    def test_rebalance(self):
        tree = BST(list(range(1, 16)))
        assert(tree.depth == 15)
        tree.rebalance()
        assert(tree.depth == 4)

    def test_traverse_in_order(self):
        tree = BST([5, 9, 7, 3, 2])
        assert(tree.traverse_in_order() == [2, 3, 5, 7, 9])
        assert(BST().traverse_in_order() == [])

    def test_traverse_level_order(self):
        tree = BST([5, 9, 7, 3, 2])
        expected = [[5], [3, 9], [2, None, 7, None]]
        assert(tree.traverse_level_order() == expected)
        assert(BST().traverse_level_order() == [])

    def test_traverse_paths(self):
        tree = BST([5, 9, 7, 3, 2])
        expected = [[5, 3, 2], [5, 9, 7]]
        assert(tree.traverse_paths() == expected)

    def test_has_path_sum(self):
        tree = BST([5, 9, 7, 3, 2])
        assert(tree.has_path_sum(10))
        assert(tree.has_path_sum(21))
        assert(not tree.has_path_sum(17))
        assert(BST().has_path_sum(0))
        assert(BST([4]).has_path_sum(4))

    def test_from_preorder(self):
        tree = BST.from_preorder([10, 5, 1, 7, 40, 50])
        assert(tree.validate())


if __name__ == '__main__':
    from random import randint
    from pprint import pprint

    # tree = BST([5, 2, 8, 1, 3, 7, 9])
    # for i in range(0, 8):
    #     tree.insert(randint(0, 100))
    # tree.rebalance()
    # print(tree.traverse_in_order())
    # pprint(tree.traverse_level_order())
    # pprint(tree.traverse_paths())

    tree = BST.from_preorder([10, 5, 1, 7, 40, 50])
    # pprint(tree.traverse_level_order())

    for o in tree.gen_inorder():
        print(o)
