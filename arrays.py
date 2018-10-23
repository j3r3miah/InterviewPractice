
def print_matrix(M):
    for y in range(len(M)):
        for x in range(len(M)):
            print(M[y][x], end=' ')
        print()
    print()


def rotate_matrix(M):
    def rotate(M, start, mlen):
        if mlen <= 1:
            return
        end = start + mlen - 1
        for i in range(start, end):
            temp = M[i][start]
            M[i][start] = M[start][end-i]
            M[start][end-i] = M[end-i][end]
            M[end-i][end] = M[end][start+i]
            M[end][start+i] = temp
        rotate(M, start + 1, mlen - 2)

    rotate(M, 0, len(M))
    return M



if __name__ == '__main__':
    M = [
        ['a','b','c','d','e'],
        ['f','g','h','i','j'],
        ['k','l','m','n','o'],
        ['p','q','r','s','t'],
        ['u','v','w','x','y'],
    ]
    # M = [
    #     [1, 2],
    #     [3, 4],
    # ]
    print_matrix(M)
    print_matrix(rotate_matrix(M))
    # print_matrix(rotate_matrix(M))
    # print_matrix(rotate_matrix(M))
    # print_matrix(rotate_matrix(M))
