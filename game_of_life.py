from pprint import pprint


def gameOfLife(board):
    """
    :type board: List[List[int]]
    :rtype: void Do not return anything, modify board in-place instead.
    """

    # 0: dead
    # 1: live
    # 2: dead->live
    # 3: live->dead
    def is_live(v):
        return v == 1 or v == 3
    
    def count_neighbors(board, i, j):
        count = 0
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if x == i and y == j:
                    continue
                if x >= 0 and x < len(board) and y >= 0 and y < len(board[0]):
                    if is_live(board[x][y]):
                        count += 1
        return count
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            live_neighbors = count_neighbors(board, i, j)
            if is_live(board[i][j]):
                if live_neighbors != 2 and live_neighbors != 3:
                    board[i][j] = 3
            else:
                if live_neighbors == 3:
                    board[i][j] = 2
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 2:
                board[i][j] = 1
            elif board[i][j] == 3:
                board[i][j] = 0


if __name__ == '__main__':
    N,M = 46,26
    board = []
    for i in range(N):
        board.append([0]*M)

    for i in range(0, N, 3):
        for j in range(0, M, 3):
            board[i][j] = 1

    for i in range(5):
        for j in range(3):
            board[i][j] = 1

    print('--- Iteration 0 ------------------------------------------')
    pprint(board)

    for i in range(100):
        gameOfLife(board)
        print()
        print(f'--- Iteration {i} ------------------------------------------')
        pprint(board)
