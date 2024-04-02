import sys
from collections import deque

t = int(sys.stdin.readline())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dq = deque()
visited = set()

for repeat in range(t):
    w,h = map(int, sys.stdin.readline().split())
    # +가 탈출구 / 불은 .에만 퍼진다
    arr = [list(sys.stdin.readline().rstrip())+["+"] for line in range(h)]
    arr.append(["+" for i in range(w+1)])
    dq.clear()
    visited.clear()

    for x in range(h):
        for y in range(w):
            # 불이 먼저 퍼지게 하고
            if arr[x][y] == "*":
                dq.appendleft((x, y, False, 0))
            # 사람이 나중에 이동하도록, 사람 또한 빈칸으로 처리한다.
            elif arr[x][y] == "@":
                arr[x][y] = "."
                dq.append((x,y,True, 0))
                visited.add((x,y))

    exit_flag = False
    while dq and not exit_flag:
        x,y,is_man, time = dq.popleft()
        if is_man:  # 사람이라면
            for d in range(4):
                next_x = x + dx[d]
                next_y = y + dy[d]
                if arr[next_x][next_y] == "+":
                    print(time+1)
                    exit_flag = True
                    break
                elif arr[next_x][next_y] ==".":
                    if (next_x, next_y) not in visited:
                        dq.append((next_x,next_y,True, time+1))
                        visited.add((next_x, next_y))

        else: # 불이라면
            for d in range(4):
                next_x = x + dx[d]
                next_y = y + dy[d]
                # 빈공간이라면 불을 퍼트린다. / 불, 벽, 탈출구로는 퍼지지 않는다.
                if arr[next_x][next_y] == ".":
                    arr[next_x][next_y] = "*"
                    dq.append((next_x, next_y, False, time + 1))
    if not exit_flag:
        print("IMPOSSIBLE")