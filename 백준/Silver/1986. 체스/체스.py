import sys

n,m = map(int, sys.stdin.readline().split())

board = [[0 for i in range(m)] for i in range(n)]

# -1이 위험, 0이 안전, 1이 퀸, 2가 나이트. 3이 폰
for i in range(1, 4):
    input_list = list(map(int, sys.stdin.readline().split()))
    count = input_list[0]
    for j in range(count):
        x = input_list[(2*j)+1] -1
        y = input_list[(2*j)+2] -1
        board[x][y] = i

# for row in board:
#     print(row)

def make_knight_move(i,j):
    global board
    dx = [-2,-1,1,2,2,1,-1,-2]
    dy = [-1,-2,-2,-1,1,2,2,1]

    for d in range(8):
        next_x = i + dx[d]
        next_y = j  +dy[d]
        if (0<=next_x<len(board)) and (0<=next_y<len(board[0])):
            if board[next_x][next_y] == 0:
                board[next_x][next_y] = -1

def make_queen_move(i,j):
    global board
    dx = [-1,1,0,0, -1,-1,1,1]
    dy = [0,0,-1,1, -1,1,1,-1]

    for d in range(8):
        next_x = i + dx[d]
        next_y = j + dy[d]
        while (0<=next_x<len(board)) and (0<=next_y<len(board[0])):
            if board[next_x][next_y] == 0 or board[next_x][next_y] == -1:
                board[next_x][next_y] = -1
                next_x += dx[d]
                next_y += dy[d]
                continue
            else:
                break
for i in range(n):
    for j in range(m):
        if board[i][j] == 1:
            make_queen_move(i,j)
        if board[i][j] ==2:
            make_knight_move(i,j)

count = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            count += 1
print(count)