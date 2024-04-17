import sys
from collections import deque

r,c = map(int, sys.stdin.readline().split())

arr = [list(sys.stdin.readline().rstrip())+["#"] for i in range(r)]
arr.append(["#" for i in range(c+1)])

dq = deque()
dx = [-1,1,0,0]
dy = [0,0,-1,1]
total_live_sheep = 0
total_live_wolf = 0

for x in range(r):
    for y in range(c):
        if arr[x][y] == "#":
            continue

        sheep = 0
        wolf = 0
        if arr[x][y] == "o":
            sheep += 1
        if arr[x][y] == "v":
            wolf += 1

        dq.append((x,y))
        arr[x][y] = "#"

        while dq:
            current_x,current_y = dq.pop()

            for d in range(4):
                next_x = current_x + dx[d]
                next_y = current_y + dy[d]

                if arr[next_x][next_y] == "#":
                    continue
                if arr[next_x][next_y] == "o":
                    sheep += 1
                if arr[next_x][next_y] == "v":
                    wolf += 1
                dq.append((next_x, next_y))
                arr[next_x][next_y] = "#"
        if sheep > wolf:
            total_live_sheep += sheep
        else:
            total_live_wolf += wolf

print(total_live_sheep, total_live_wolf)