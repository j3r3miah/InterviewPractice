from collections import namedtuple
from pprint import pprint

Point = namedtuple('Point', ['i', 'j'])

def flood_fill(M, start_row, start_col, new_color):
    start = Point(start_row, start_col)
    orig_color = M[start.i][start.j]
    if orig_color == new_color:
        return

    def neighbors(M, p):
        if p.i > 0:
            yield Point(p.i-1, p.j)
        if p.i + 1 < len(M):
            yield Point(p.i+1, p.j)
        if p.j > 0:
            yield Point(p.i, p.j-1)
        if p.j + 1 < len(M[0]):
            yield Point(p.i, p.j+1)

    stack = [start]
    while stack:
        print()
        pprint(M)
        p = stack.pop()
        print('popped:', p.i, p.j)
        M[p.i][p.j] = new_color
        for n in neighbors(M, p):
            if M[n.i][n.j] == orig_color:
                stack.append(n)


def test_flood_file():
    rows, cols = 40, 20
    M = [[0]*cols for _ in range(rows)]

    for i in range(12, 23):
        for j in range(5, 18):
            M[i][j] = 1
    for i in range(18, 20):
        for j in range(9, 16):
            M[i][j] = 0

    pprint(M)
    flood_fill(M, 0, 0, 5)
    print()
    pprint(M)
    flood_fill(M, 19, 10, 3)
    print()
    pprint(M)
    flood_fill(M, 12, 5, 7)
    print()
    pprint(M)


if __name__ == '__main__':
    M = [[0,0,0],[0,1,1]]
    pprint(M)
    flood_fill(M, 1, 1, 1)
    # print()
    # pprint(M)
