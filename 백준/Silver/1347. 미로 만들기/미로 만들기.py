import sys

length = int(sys.stdin.readline())
memo = list(sys.stdin.readline().rstrip())

#direction은 %로 표현(하좌상우)
direction = 0
x_dir = (1, 0, -1, 0)
y_dir = (0, -1, 0, 1)

#최대로 가면 한쪽으로만 50번 가는것
maze = [['#' for i in range(101)] for j in range(101)]

current_x = 50
current_y = 50

maze[current_x][current_y] = '.'

min_x = 50
max_x = 50
min_y = 50
max_y = 50

for command in memo:
    #L이면 왼쪽으로 방향만 전환
    if command == 'L':
        direction = (direction-1)%4
        continue
    #R이면 오른쪽으로 방향만 전환
    if command == 'R':
        direction = (direction+1)%4
        continue

    #F라면 이동한 다음 점 찍고
    current_x = current_x + x_dir[direction]
    current_y = current_y + y_dir[direction]
    maze[current_x][current_y] = '.'

#min / max xy 업데이트
    min_x = min(min_x, current_x)
    max_x = max(max_x, current_x)
    min_y = min(min_y, current_y)
    max_y = max(max_y, current_y)

#min/max에 따라 적절히 미로를 자름
for x in range(min_x, max_x+1):
    for y in range(min_y, max_y+1):
        print(maze[x][y], end="")
    print('')