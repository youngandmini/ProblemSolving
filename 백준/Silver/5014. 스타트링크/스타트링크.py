import sys
from collections import deque

floor, start, goal, up, down = map(int, sys.stdin.readline().split())

elevator = [-1 for i in range(floor+1)]
elevator[start] = 0

buttons = [up, -down]

dq = deque()
dq.append(start)

while dq:
    current = dq.popleft()

    for move in buttons:
        next = current+move

        if 1<=next<=floor and elevator[next] == -1:
            dq.append(next)
            elevator[next] = elevator[current] +1

if elevator[goal] == -1:
    print("use the stairs")
else:
    print(elevator[goal])