
class Hash:
    empty = 'empty'
    A = [None] * 8
    size = 0

    def __init__(self, capacity=None):
        if capacity:
            self.A = [None] * capacity

    def dump(self):
        print(f'len={self.len()} :: {self.A}')

    def hash(self, key):
        h = 0
        for i, c in enumerate(key):
            h += (i + 1) * ord(c)
        rv = h % len(self.A)
        print(f'hash("{key}") = {rv}')
        return rv

    def add(self, key, value):
        if self.size == len(self.A):
            self.rehash()
        h = self.hash(key)
        i = h
        while self.A[i] != None and self.A[i] != self.empty:
            print('Probing...')
            i += 1
            if i == len(self.A):
                i = 0
        self.A[i] = (key, value)
        self.size += 1

    def rehash(self):
        print('Rehash!')
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
            if self.A[i] != self.empty and self.A[i][0] == key:
                return self.A[i][1]
            i += 1
            if i == len(self.A):
                i = 0
                looped = True
        return None

    def delete(self, key):
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

    def len(self):
        return self.size


if __name__ == '__main__':
    h = Hash(4)
    h.add('foo', 'My name is foo')
    h.add('bar', 'I like to go to bars')
    h.add('baz', 'And baz out all night')
    print(h.get('bar'))
    print(h.get('baz'))
    print(h.get('foo'))
    h.dump()
    h.delete('baz')
    print(h.get('baz'))
    h.delete('bar')
    h.delete('foo')
    h.add('baz', 'Baz out')
    h.add('bar', 'Go to bars')
    h.add('foo', 'Name is foo')
    h.add('Jeremiah', 36)
    h.add('Tierrany', 33)
    h.add('Colleen', 55)
    h.add('Solo', 5)
    h.add('Rasta', 8)
    h.dump()
    h.add('REHASH!', 'Now?')
    h.dump()
    print(h.get('Solo'))
