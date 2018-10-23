# from sys import maxint


class Node:
    data = None
    left = None
    right = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return str(self.data)


def insert(A):
    _insert(A, 0, len(A) - 1)


def _insert(A, start, end):
    if end < start:
        return
    mid = int((start + end) / 2)
    print(A[mid])
    _insert(A, start, mid - 1)
    _insert(A, mid + 1, end)


def balanced(root):
    return _height(root) != -1


def _height(root):
    if not root:
        return 0
    left_height = _height(root.left)
    if left_height == -1:
        return -1
    right_height = _height(root.right)
    if right_height == -1:
        return -1
    if abs(left_height - right_height) >= 1:
        return -1
    return 1 + max(left_height, right_height)


_last = None
def validate_bst_1(root):
    global _last
    if not root:
        return True
    if not validate_bst_1(root.left):
        return False
    if _last and root.data <= _last:
        return False
    _last = root.data
    if not validate_bst_1(root.right):
        return False


def validate_bst_2(root):
    return _check_bst(root, -maxint - 1, maxint)


def _check_bst(root, min, max):
    if not root:
        return True
    return (
        root.data > min and
        root.data <= max and
        _check_bst(root.left, min, root.data) and
        _check_bst(root.right, root.data, max)
    )


_predecessor = None
def successor(root, node):
    global _predecessor
    if root:
        rv = successor(root.left, node)
        if rv:
            return rv
        if _predecessor == node:
            return root
        _predecessor = node
        rv = successor(root.right, node)
        if rv:
            return rv
    return None


def LCA(root, n1, n2):
    # root is a binary (*not* bst) tree
    return _LCA(root, n1, n2)[2]


def _LCA(root, n1, n2):
    if not root:
        return (False, False, None)
    if root == n1 and root == n2:
        return (True, True, root)
    left = _LCA(root.left, n1, n2)
    if left[2]:
        return left
    right = _LCA(root.right, n1, n2)
    if right[2]:
        return right
    found_n1 = left[0] or right[0]
    found_n2 = left[1] or right[1]
    if found_n1 and found_n2:
        return (True, True, root)
    if (found_n1 or found_n2) and (root == n1 or root == n2):
        return (True, True, root)
    return (
        found_n1 or root == n1,
        found_n2 or root == n2,
        None
    )


if __name__ == '__main__':
    # insert([1, 5, 9, 10, 11, 14, 16, 20])

    a = Node('A')
    a.left = Node('B')
    a.left.left = Node('D')
    a.left.right = Node('E')
    a.left.right.left = Node('H')
    a.right = Node('C')
    a.right.left = Node('F')
    a.right.left.right = Node('I')
    a.right.left.right.left = Node('J')
    a.right.left.right.right = Node('K')
    a.right.right = Node('G')

    root = a
    n1 = a.left.left
    n2 = a.left.right.left

    print(f'LCA of {n1} and {n2} is {LCA(root, n1, n2)}')
