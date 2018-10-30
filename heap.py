import pytest


class MinHeap:
    def __init__(self, items=None, capacity=8):
        self.A = [None]*capacity
        self.count = 0
        if items:
            for o in items:
                self.push(o)

    def push(self, data):
        # expand storage if necessary
        if self.count == len(self.A):
            self._grow()
        # insert new element at end of list
        i = self.count
        self.A[i] = data
        self.count += 1
        # sift up until heap is restored
        while i > 0 and self.A[i//2] > data:
            self._swap(i, i//2)
            i = i//2

    def peek(self):
        if self.count == 0:
            return None
        return self.A[0]

    def pop(self):
        if self.count == 0:
            return None
        # replace min element with last element
        rv = self.A[0]
        self.A[0] = self.A[self.count-1]
        self.A[self.count-1] = None
        self.count -= 1
        # sift down until heap is restored
        self._sift_down()
        return rv

    def replace(self, data):
        if self.count == 0:
            self.push(data)
            return None
        # replace min element with last element
        rv = self.A[0]
        self.A[0] = data
        # sift down until heap is restored
        self._sift_down()
        return rv

    def _sift_down(self):
        i = 0
        while i < self.count:
            left = 2*i+1
            right = 2*i+2
            smaller = self.A[i]
            smaller_i = None
            if (
                left < self.count and
                self.A[left] is not None and
                self.A[left] < smaller
            ):
                smaller = self.A[left]
                smaller_i = left
            if (
                right < self.count and
                self.A[right] is not None and
                self.A[right] < smaller
            ):
                smaller_i = right

            if smaller_i:
                self._swap(i, smaller_i)
                i = smaller_i
            else:
                break

    def _swap(self, x, y):
        self.A[x], self.A[y] = self.A[y], self.A[x]

    def _grow(self):
        tmp = self.A
        self.A = [None] * (len(tmp) * 2)
        for i in range(self.count):
            self.A[i] = tmp[i]

    def __len__(self):
        return self.count


class TestMinHeap:
    def test_push(self):
        heap = MinHeap([5, 3, 8, 9, 1])
        assert(heap.A == [1, 3, 5, 9, 8, None, None, None])

    def test_pop(self):
        heap = MinHeap([5, 3, 8, 9, 1])
        assert(len(heap) == 5)
        assert(heap.pop() == 1)
        assert(heap.A == [3, 8, 5, 9, None, None, None, None])
        assert(heap.pop() == 3)
        assert(heap.A == [5, 8, 9, None, None, None, None, None])
        assert(heap.pop() == 5)
        assert(heap.A == [8, 9, None, None, None, None, None, None])
        assert(heap.pop() == 8)
        assert(heap.A == [9, None, None, None, None, None, None, None])
        assert(heap.pop() == 9)
        assert(heap.A == [None, None, None, None, None, None, None, None])
        assert(len(heap) == 0)

    def test_peek(self):
        heap = MinHeap([5, 3, 8, 9, 1])
        assert(heap.peek() == 1)
        heap.pop()
        assert(heap.peek() == 3)

    def test_replace(self):
        heap = MinHeap([5, 3, 8, 9, 1])
        assert(heap.replace(0) == 1)
        assert(heap.A == [0, 3, 5, 9, 8, None, None, None])
        assert(heap.replace(7) == 0)
        assert(heap.A == [3, 7, 5, 9, 8, None, None, None])

    def test_grow(self):
        heap = MinHeap([5, 3, 8, 9], capacity=4)
        assert(len(heap) == 4)
        heap.push(10)
        assert(len(heap) == 5)
        assert(len(heap.A) == 8)
