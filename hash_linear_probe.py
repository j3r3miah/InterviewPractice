from pprint import pprint
from collections import namedtuple

Pair = namedtuple('Pair', ['key', 'value'])


class Hash:
    empty = 'empty'
    A = [None] * 8
    size = 0

    def __init__(self, capacity=None):
        if capacity:
            self.A = [None] * capacity

    def hash(self, key):
        h = 0
        for i, c in enumerate(key):
            h += (i + 1) * ord(c)
        rv = h % len(self.A)
        # print(f'hash("{key}") = {rv}')
        return rv

    def add(self, key, value):
        if self.size == len(self.A):
            self.rehash()
        h = self.hash(key)
        i = h
        while self.A[i] != None and self.A[i] != self.empty:
            # print('Probing...')
            i += 1
            if i == len(self.A):
                i = 0
        self.A[i] = Pair(key, value)
        self.size += 1

    def rehash(self):
        # print('Rehash!')
        F = self.A
        self.A = [None] * (len(F) * 2)
        self.size = 0
        for i in range(0, len(F)):
            x = F[i]
            if x != None and x != self.empty:
                self.add(*x)

    def get(self, key):
        h = self.hash(key)
        looped = False
        i = h
        while self.A[i] != None and not (looped and i == h):
            if self.A[i] != self.empty and self.A[i].key == key:
                return self.A[i].value
            i += 1
            if i == len(self.A):
                i = 0
                looped = True
        return None

    def remove(self, key):
        h = self.hash(key)
        looped = False
        i = h
        while self.A[i] != None and not (looped and i == h):
            if self.A[i] != self.empty and self.A[i][0] == key:
                self.A[i] = self.empty
                self.size -= 1
            i += 1
            if i == len(self.A):
                i = 0
                looped = True

    def keys(self):
        for o in self.A:
            if o is not None and o != self.empty:
                yield o.key

    def values(self):
        for o in self.A:
            if o is not None and o != self.empty:
                yield o.value

    def pairs(self):
        for o in self.A:
            if o is not None and o != self.empty:
                yield o

    def _dump(self):
        lf = self.size / len(self.A)
        print(f'Capacity={len(self.A)}, Size={self.size}, Load Factor={lf}')
        pprint(self.A)

    def __len__(self):
        return self.size


if __name__ == '__main__':
    h = Hash(4)
    h.add('foo', 'My name is foo')
    h.add('bar', 'I like to go to bars')
    h.add('baz', 'And baz out all night')
    print(len(h))
    print(list(h.keys()))
    del h['foo']
    print(len(h))
    print(list(h.keys()))
    # print(h.get('bar'))
    # print(h.get('baz'))
    # print(h.get('foo'))
    # h._dump()
    # h.remove('baz')
    # print(h.get('baz'))
    # h.remove('bar')
    # h.remove('foo')
    # h.add('baz', 'Baz out')
    # h.add('bar', 'Go to bars')
    # h.add('foo', 'Name is foo')
    # h.add('Jeremiah', 36)
    # h.add('Tierrany', 33)
    # h.add('Colleen', 55)
    # h.add('Solo', 5)
    # h.add('Rasta', 8)
    # h._dump()
    # h.add('REHASH!', 'Now?')
    # h._dump()
    # print(h.get('Solo'))
