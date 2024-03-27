import sys

n = int(sys.stdin.readline())

arr = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

dp_table = [[0 for j in range(n)] for i in range(n)]
dp_table[0][0] = 1

for i in range(n):
    for j in range(n):
        if i == n-1 and j == n-1:
            break

        #세로 점프
        if i + arr[i][j] < n:
            dp_table[i+arr[i][j]][j] += dp_table[i][j]
        #가로 점프
        if j+arr[i][j] < n:
            dp_table[i][j + arr[i][j]] += dp_table[i][j]

print(dp_table[-1][-1])