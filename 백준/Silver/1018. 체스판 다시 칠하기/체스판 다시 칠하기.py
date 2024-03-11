import sys

n, m = map(int, sys.stdin.readline().split())

board = []
for i in range(n):
    board.append(list(sys.stdin.readline().rstrip()))

min_count = sys.maxsize
bw_seq = ["B", "W"]

for i in range(n-7):
    for j in range(m-7):

        #bw 순서 검사
        count = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if board[x][y] != bw_seq[(x+y)%2]:
                    count += 1
        min_count = min(min_count, count)

        #wb 순서 검사
        count = 0
        for x in range(i, i + 8):
            for y in range(j, j + 8):
                if board[x][y] != bw_seq[(x + y +1) % 2]:
                    count += 1
        min_count = min(min_count, count)
print(min_count)