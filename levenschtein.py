
def _edit_distance(s, t):
    m = len(s) + 1
    n = len(t) + 1
    d = []
    for i in range(m):
        d.append([None] * n)

    for i in range(m):
        d[i][0] = i

    for j in range(n):
        d[0][j] = j

    for j in range(1, n):
        for i in range(1, m):
            if s[i-1] == t[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = 1 + min(
                    d[i-1][j],
                    d[i][j-1],
                    d[i-1][j-1]
                )

    return d[m-1][n-1]


def __edit_distance(s, t, m=None, n=None):
    if m is None:
        m = len(s)
    if n is None:
        n = len(t)

    if m == 0:
        return n

    if n == 0:
        return m

    if s[m-1] == t[n-1]:
        return edit_distance(s, t, m-1, n-1)

    return 1 + min(
        edit_distance(s, t, m-1, n),
        edit_distance(s, t, m, n-1),
        edit_distance(s, t, m-1, n-1)
    )


def edit_distance(s, t, m=None, n=None, memo=None):
    m = len(s) if m is None else m
    n = len(t) if n is None else n
    memo = {} if memo is None else memo

    if m == 0:
        return n

    if n == 0:
        return m

    if (m, n) not in memo:
        if s[m-1] == t[n-1]:
            memo[(m, n)] = edit_distance(s, t, m-1, n-1)
        else:
            memo[(m, n)] = 1 + min(
                edit_distance(s, t, m-1, n),
                edit_distance(s, t, m, n-1),
                edit_distance(s, t, m-1, n-1)
            )
    return memo[(m, n)]


def test_edit_distance():
    for pair in [
        ('sitting', 'kitten'),
        ('Sunday', 'Saturday'),
    ]:
        distance = edit_distance(pair[0], pair[1])
        print(f'{pair[0]} => {pair[1]} = {distance}')


if __name__ == '__main__':
    import sys
    if len(sys.argv) == 3:
        s = sys.argv[1]
        t = sys.argv[2]
        distance = edit_distance(s, t)
        print(f'{s} => {t} = {distance}')
    else:
        test_edit_distance()
