import sys

r,c,t = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for i in range(r)]

conditioner_x = 0

for i in range(r):
    if arr[i][0] == -1:
        conditioner_x = i+1
        break
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def before_conditioning():
    global r,c,arr, conditioner_x,dx , dy
    expanded_arr = []

    for x in range(r):
        for y in range(c):
            # 미세먼지가 없거나, 공기청정기라면 스킵
            if arr[x][y] <= 0:
                continue
            expand_amount = arr[x][y]//5
            for d in range(4):
                next_x = x+dx[d]
                next_y = y+dy[d]
                if 0<=next_x<r and  0<=next_y<c and arr[next_x][next_y] != -1:
                    arr[x][y]  = arr[x][y] - expand_amount
                    expanded_arr.append((next_x, next_y, expand_amount))
    while expanded_arr:
        expand_x, expand_y, expand_amount = expanded_arr.pop()
        arr[expand_x][expand_y] += expand_amount

def upper_cycle():
    global r, c, arr, conditioner_x
    # 왼쪽 사이드
    for x in range(conditioner_x-3, -1, -1):
        arr[x+1][0] = arr[x][0]
    # 위쪽 사이드
    for y in range(c-1):
        arr[0][y] = arr[0][y+1]
    # 오른쪽 사이드
    for x in range(conditioner_x-1):
        arr[x][c-1] = arr[x+1][c-1]
    # 아래쪽 사이드
    for y in range(c-1, 1, -1):
        arr[conditioner_x-1][y] = arr[conditioner_x-1][y-1]
    arr[conditioner_x-1][1] = 0

def lower_cycle():
    global r, c, arr, conditioner_x
    # 왼쪽 사이드
    for x in range(conditioner_x +1, r-1):
        arr[x][0] = arr[x+1][0]
    # 아래쪽 사이드
    for y in range(c-1):
        arr[r-1][y] = arr[r-1][y + 1]
    # 오른쪽 사이드
    for x in range(r-1, conditioner_x, -1):
        arr[x][c - 1] = arr[x - 1][c - 1]
# 위쪽 사이드
    for y in range(c-1, 1, -1):
        arr[conditioner_x][y] = arr[conditioner_x][y-1]
    arr[conditioner_x][1] = 0

for repeat in range(t):
    before_conditioning()
    upper_cycle()
    lower_cycle()

total_dust = 2
for row in arr:
    for element in row:
        total_dust += element
print(total_dust)