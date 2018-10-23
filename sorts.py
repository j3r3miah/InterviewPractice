
def mergesort(A):
    def _mergesort(A, B, start, end, indent=''):
        if end <= start:
            return

        mid = int((end + start) / 2)
        _mergesort(A, B, start, mid, indent + '  ')
        _mergesort(A, B, mid + 1, end, indent + '  ')

        for i in range(start, end + 1):
            B[i] = A[i]

        l = start
        r = mid + 1
        for i in range(start, end + 1):
            if l <= mid and (r > end or B[l] < B[r]):
                A[i] = B[l]
                l += 1
            else:
                A[i] = B[r]
                r += 1

    B = [None] * len(A)
    _mergesort(A, B, 0, len(A) - 1)
    return A


def quicksort(A):
    def _quicksort(A, low, high, indent=''):
        if low < high:
            last_pivot = _partition(A, low, high, indent)
            _quicksort(A, low, last_pivot - 1, indent + '   ')
            _quicksort(A, last_pivot, high, indent + '   ')

    def _partition(A, left, right, indent=''):
        pivot_index = int((left + right) / 2)  # pivot about midpoint
        pivot = A[pivot_index]
        print(indent, 'pivot =', pivot, A)
        while left < right:
            print(indent, 'left =', left)
            print(indent, 'right =', right)
            while A[left] < pivot:
                left += 1
            while pivot < A[right]:
                right -= 1

            if left <= right:
                A[left], A[right] = A[right], A[left]
                print(indent, '   swapped ', left, right, A)
                if pivot_index == left:
                    pivot_index = right
                elif pivot_index == right:
                    pivot_index = left
                left += 1
                right -= 1

        print(indent, 'returning', pivot_index, '->', A[pivot_index])
        return left

    _quicksort(A, 0, len(A) - 1)
    return A


if __name__ == '__main__':
    import random
    # A = [random.randint(0, 25) for _ in range(0, 20)]
    # A = [9, 16, 20, 18, 14, 10, 15, 21, 5, 12, 28]
    # print(A)
    # print(mergesort(A))
    # print(quicksort(A))
    for i in range(1, 1000):
        A = [random.randint(0, 99) for _ in range(0, 20)]
        assert mergesort(A) == quicksort(A)
