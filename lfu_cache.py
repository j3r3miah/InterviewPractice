from collections import OrderedDict, defaultdict


class LFUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.dict = {}  # key => (value, frequency)
        self.cache = defaultdict(OrderedDict)  # frequency => { key => key }

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dict:
            return -1
        value, frequency = self.dict[key]
        self.dict[key] = (value, frequency+1)
        del self.cache[frequency][key]
        if len(self.cache[frequency]) == 0:
            del self.cache[frequency]
        self.cache[frequency+1][key] = True
        return value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity == 0:
            return

        if key in self.dict:
            self.get(key)
            _, frequency = self.dict[key]
            self.dict[key] = (value, frequency)
            return

        if self.size == self.capacity:
            min_freq = min(self.cache.keys())
            removed_key, _ = self.cache[min_freq].popitem(last=False)
            del self.dict[removed_key]
            self.size -= 1

        self.dict[key] = (value, 0)
        self.cache[0][key] = True
        self.size += 1

    def dump(self):
        for frequency in self.cache.keys():
            for key in self.cache[frequency]:
                print(f'Key={key}, Hits={frequency}')
        print()
        for key, value in self.dict.items():
            print(f'{key} :: {value}')


if __name__ == '__main__':

    # cmd = ["LFUCache","put","put","get","put","get","get","put","get","get","get"]
    # arg = [[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]

    cmd = ["LFUCache","put","put","put","put","put","get","put","get","get","put","get","put","put","put","get","put","get","get","get","get","put","put","get","get","get","put","put","get","put","get","put","get","get","get","put","put","put","get","put","get","get","put","put","get","put","put","put","put","get","put","put","get","put","put","get","put","put","put","put","put","get","put","put","get","put","get","get","get","put","get","get","put","put","put","put","get","put","put","put","put","get","get","get","put","put","put","get","put","put","put","get","put","put","put","get","get","get","put","put","put","put","get","put","put","put","put","put","put","put"]
    arg = [[10],[10,13],[3,17],[6,11],[10,5],[9,10],[13],[2,19],[2],[3],[5,25],[8],[9,22],[5,5],[1,30],[11],[9,12],[7],[5],[8],[9],[4,30],[9,3],[9],[10],[10],[6,14],[3,1],[3],[10,11],[8],[2,14],[1],[5],[4],[11,4],[12,24],[5,18],[13],[7,23],[8],[12],[3,27],[2,12],[5],[2,9],[13,4],[8,18],[1,7],[6],[9,29],[8,21],[5],[6,30],[1,12],[10],[4,15],[7,22],[11,26],[8,17],[9,29],[5],[3,4],[11,30],[12],[4,29],[3],[9],[6],[3,4],[1],[10],[3,29],[10,28],[1,20],[11,13],[3],[3,12],[3,8],[10,9],[3,26],[8],[7],[5],[13,17],[2,27],[11,15],[12],[9,19],[2,15],[3,16],[1],[12,17],[9,1],[6,19],[4],[5],[5],[8,1],[11,7],[5,2],[9,28],[1],[2,2],[7,4],[4,22],[7,24],[9,26],[13,28],[11,26]]

    obj = None
    rv = []
    gets = []

    for o, a in zip(cmd, arg):
        if o == 'LFUCache':
            print(f'LFUCache({a[0]})')
            obj = LFUCache(a[0])
            rv.append(None)
        elif o == 'put':
            print(f'put({a[0]}, {a[1]})')
            obj.put(a[0], a[1])
            rv.append(None)
        elif o == 'get':
            print(f'get({a[0]})')
            rv.append(obj.get(a[0]))
            gets.append(rv[-1])

    print()
    obj.dump()
    print()
    print(rv)

    expected = [-1,19,17,-1,-1,-1,5,-1,12,3,5,5,1,-1,30,5,30,-1,-1,24,18,14,18,11,18,-1,4,29,30,12,11,29,17,-1,18,-1,20,29,18,18,20]
    print()
    print(gets)
    print(expected)
