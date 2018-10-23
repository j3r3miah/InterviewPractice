from pprint import pprint

if __name__ == '__main__':
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
