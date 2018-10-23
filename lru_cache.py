from collections import OrderedDict


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = self.tail = None

    def append(self, node):
        if self.tail is None:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        return node
            
    def popfirst(self):
        if self.head:
            node = self.head
            if self.head.next:
                self.head.next.prev = None
            self.head = self.head.next
            return node
        return None
    
    def remove(self, node):
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        node.prev = None
        node.next = None


class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.count = 0
        self.map = {}
        self.list = LinkedList()
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.map:
            self._touch(key)
            return self.map[key].value
        return -1
    
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.map:
            node = self.map[key]
            self.list.remove(node)
            del self.map[node.key]
            self.count -= 1

        if self.count == self.capacity:
            node = self.list.popfirst()
            del self.map[node.key]
            self.count -= 1

        node = Node(key, value)
        self.list.append(node)
        self.map[key] = node
        self.count += 1
    
    def _touch(self, key):
        node = self.map[key]
        # remove node from place in list
        self.list.remove(node)
        # re-add node at tail of list
        self.list.append(node)


class LRUCache2:
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = OrderedDict()

    def put(self, key, value):
        self.map[key] = value
        if len(self.map) > self.capacity:
            self.map.popitem(last=False)

    def get(self, key):
        if key in self.map:
            self.map.move_to_end(key)
            return self.map.get(key)
        return -1


if __name__ == '__main__':
    cmds = ["LRUCache","put","put","get","put","get","put","get","get","get"]
    args = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
    # cmds = ["LRUCache","put","put","get","put","put","get"]
    # args = [[2],[2,1],[2,2],[2],[1,1],[4,1],[2]]
    # cmds = ["LRUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
    # args = [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]

    lru = None
    rv = []
    for i in range(len(cmds)):
        cmd = cmds[i]
        arg = args[i]
        if cmd == 'LRUCache':
            lru = LRUCache2(arg[0])
            print('Capacity = ' + str(arg[0]))
            rv.append('null')
        elif cmd == 'put':
            lru.put(arg[0], arg[1])
            rv.append('null')
            print(f'Put({arg[0]}, {arg[1]})')
        elif cmd == 'get':
            val = lru.get(arg[0])
            rv.append(val)
            print(f'Get({arg[0]}, {val})')

    print(','.join([str(o) for o in rv]))
