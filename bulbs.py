def bulbs(A):
    count = 0
    off = 0
    i = 0
    while i < len(A):
        if A[i] == off:
            count += 1
            off = 1 - off
        i += 1
    return count




if __name__ == '__main__':
    for o in [
        [0, 1, 0, 1],
        [1, 1, 0, 1],
        [0, 0, 1, 1],
    ]:
        print(o)
        print(bulbs(o))
        print()
