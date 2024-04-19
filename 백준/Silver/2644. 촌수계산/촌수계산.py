import sys
from collections import deque

n = int(sys.stdin.readline())
start, target = map(int,sys.stdin.readline().split())

m = int(sys.stdin.readline())
graph = [[] for i in range(n+1 )]

for repeat in range(m):
    x, y = map(int, sys.stdin.readline().split())
    graph[x].append(y)
    graph[y].append(x)

dq = deque()
visited = set()

dq.append((start, 0))
visited.add(start)

while dq:
    man, depth = dq.popleft()
    if man == target:
        print(depth)
        break
    for next_man in graph[man]:
        if next_man not in visited:
            dq.append((next_man, depth+1))
            visited.add(next_man)
else:
    print(-1)