
#1
import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

graph = {}
for i in range(1, n+1):
    graph[i] = set()
visited = set()

for i in range(m):
    u,v = map(int, sys.stdin.readline().split())
    graph[u].add(v)
    graph[v].add(u)

dq = deque()
count = 0

for node in graph:
    if node in visited:
        continue

    dq.append(node)
    visited.add(node)
    count += 1

    while dq:
        current_node = dq.popleft()
        for next_node in graph[current_node]:
            if next_node in visited:
                continue
            dq.append(next_node)
            visited.add(next_node)

print(count)