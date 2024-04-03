import sys

arr = [list(map(int, sys.stdin.readline().split())) for i in range(5)]

result_set = set()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
def recur(x, y, n, sum):
    global result

    if n == 5:
        result_set.add(sum)
        return

    for d in range(4):
        next_x = x + dx[d]
        next_y = y + dy[d]
        if (0<=next_x<5) and (0<=next_y<5):
            recur(next_x, next_y, n+1, sum*10+arr[next_x][next_y])


for i in range(5):
    for j in range(5):
        recur(i, j, 0, arr[i][j])

print(len(result_set))