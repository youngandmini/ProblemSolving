import sys

n,m = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

candy = [[0 for j in range(m)] for i in range(n)]
candy[0][0] = arr[0][0]

for j in range(1, m):
    candy[0][j] = candy[0][j-1] + arr[0][j]

for i in range(1, n):
    candy[i][0] = candy[i-1][0] + arr[i][0]

for i in range(1, n):
    for j in range(1, m):
        candy[i][j] = max(candy[i - 1][j], candy[i][j-1]) + arr[i][j]

print(candy[-1][-1])
