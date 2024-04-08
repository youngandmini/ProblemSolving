import sys
from collections import deque

# 12시부터 1시방향으로
# 3시방향은 wheel[i][2]
# 9시방향은 wheel[i][6]
wheel = [deque(list(sys.stdin.readline().rstrip())) for i in range(4)]
k = int(sys.stdin.readline())


# i: 톱니, d: 방향
def get_rotate_information(i, d):
    global wheel, rotate

    rotate.add((i,d))
    # 왼쪽 톱니바퀴
    # 비교할 왼쪽 톱니가 있고, 기존 톱니의 9시방향이 왼쪽 톱니의 3시 방향과 다르고, 아직 고려되지 않은 톱니라면
    if i-1>=0 and wheel[i][6] != wheel[i-1][2] and (i-1, (d+1)%2) not in rotate:
        get_rotate_information(i-1, (d+1)%2)
    # 비교할 오른쪽 톱니가 있고, 기존 톱니의 3시방향이 오른쪽 톱니의 9시 방향과 다르고, 아직 고려되지 않은 톱니라면
    if i+1<=3 and wheel[i][2] != wheel[i+1][6] and (i+1, (d+1)%2) not in rotate:
        get_rotate_information(i+1, (d+1)%2)

def do_rotation():
    global wheel, rotate

    for i,d in rotate:
        # 반시계
        if d == 0:
            wheel[i].append(wheel[i].popleft())
        # 시계
        else:
            wheel[i].appendleft(wheel[i].pop())

rotate = set()
for rep in range(k):
    i, d = map(int, sys.stdin.readline().split())
    # 편의를 위한 인덱스 조정
    i -= 1
    # 편의를 위한 방향 조정 - 0이면 반시계, 1이면 시계
    if d == -1:
        d = 0
    rotate.clear()
    get_rotate_information(i,d)
    do_rotation()

result = 0
for i in range(4):
    if wheel[i][0] == "1":
        result += 2**i

print(result)