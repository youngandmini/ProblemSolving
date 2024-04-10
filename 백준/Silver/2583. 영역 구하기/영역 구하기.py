import sys
from collections import deque

m,n,k = map(int, sys.stdin.readline().split())

arr = [[0 for y in range(n)]+[-1] for x in range(m)]
arr.append([-1 for y in range(n+1)])


for i in range(k):
    y1,x1,y2,x2 = map(int, sys.stdin.readline().split())
    for x in range(m-x2,m-x1):  # arr과 보기에서 주어진 row가 거꾸로다
        for y in range(y1,y2):
            arr[x][y] = -1

dx = [-1,1,0,0]
dy = [0,0,-1,1]
dq = deque()

rectangle_seq = 1
for x in range(m):
    for y in range(n):

        if arr[x][y] != 0:
            continue
        arr[x][y] = rectangle_seq
        dq.append((x,y))

        while dq:
            now_x, now_y = dq.popleft()
            for d in range(4):
                next_x = now_x + dx[d]
                next_y = now_y + dy[d]
                if arr[next_x][next_y] == 0:
                    arr[next_x][next_y] = rectangle_seq
                    dq.append((next_x, next_y))

        rectangle_seq += 1

answer = [0 for i in range(rectangle_seq)]

for row in arr:
    for element in row:
        if element != -1:
            answer[element] += 1

print(rectangle_seq-1)
print(*sorted(answer[1:]))