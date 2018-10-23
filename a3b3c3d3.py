
def naive(n=1000):
    # O(N^4)
    rv = []
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            for c in range(1, n + 1):
                for d in range(1, n + 1):
                    if a**3 + b**3 == c**3 + d**3:
                        # print(a, b, c, d)
                        rv.append((a, b, c, d))
    return rv


def faster(n=1000):
    # O(N^2)?
    values = {}
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            val = a**3 + b**3 
            values.setdefault(val, []).append((a,b))

    rv = []
    for val, pairs in values.items():
        for i in pairs:
            for j in pairs:
                # print(*(i + j))
                rv.append((i + j))
    return rv


if __name__ == '__main__':
    n = 20
    test0 = naive(n)
    test1 = faster(n)
    assert(sorted(test0) == sorted(test1))
