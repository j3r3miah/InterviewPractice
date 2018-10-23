class Node:
    data = None
    next = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return str(self.data)


class List:
    head = None

    def insert(self, data):
        new_head = Node(data)
        new_head.next = self.head
        self.head = new_head
        return self.head

    def __len__(self):
        len = 0
        cur = self.head
        while cur:
            cur = cur.next
            len += 1
        return len

    def __repr__(self):
        rv = []
        cur = self.head
        while cur:
            rv.append(cur)
            cur = cur.next
        return str(rv)


def intersection(list1, list2):
    len1 = len(list1)
    len2 = len(list2)
    if len1 > len2:
        long = list1.head
        short = list2.head
    else:
        long = list2.head
        short = list1.head
    for i in range(abs(len1 - len2)):
        long = long.next
    while long:
        if long == short:
            return long
        long = long.next
        short = short.next
    return None


def delete_duplicates(list):
    cur = list.head
    while cur.next:
        if cur.data == cur.next.data:
            cur.next = cur.next.next
        else:
            cur = cur.next


if __name__ == '__main__':
    # l1 = List()
    # for i in range(10, 0, -1):
    #     l1.insert(i)
    # l2 = List()
    # l2.insert('c')
    # l2.insert('b')
    # l2.insert('a')
    # # l2.head.next.next.next = l1.head.next.next.next.next.next
    # # l2.head = l1.head.next.next.next.next
    # print(l1)
    # print(l2)
    # print(intersection(l1, l2))

    l1 = List()
    l1.insert(1)
    # for i in range(10, 0, -1):
    #     l1.insert(i)
    #     l1.insert(i)
    #     l1.insert(i)
    print(l1)
    delete_duplicates(l1)
    print(l1)
