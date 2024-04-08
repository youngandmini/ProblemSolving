import sys

sys.setrecursionlimit(10000)

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

visited = set()

def dfs(rain, x, y):
    global arr, visited, n

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    for d in range(4):
        next_x = x+dx[d]
        next_y = y+dy[d]
        if 0<=next_x<n and 0<=next_y<n and arr[next_x][next_y] > rain and (next_x,next_y) not in visited:
            visited.add((next_x, next_y))
            dfs(rain, next_x, next_y)

max_count = 1
for rain in range(1, 100):
    visited.clear()
    count = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > rain and (i, j) not in visited:
                count += 1
                visited.add((i, j))
                dfs(rain, i, j)
    max_count = max(max_count, count)
print(max_count)