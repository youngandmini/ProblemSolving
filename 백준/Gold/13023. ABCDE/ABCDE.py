import sys

n, m = map(int, sys.stdin.readline().split())

graph = {}
for i in range(n):
    graph[i] = set()

for i in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].add(b)
    graph[b].add(a)

def dfs(a, count):
    global graph, visited, flag

    if flag:
        return

    if count == 4:
        flag = True

    for b in graph[a]:
        if b in visited:
            continue
        visited.add(b)
        dfs(b, count+1)
        visited.remove(b)

visited = set()
flag = False

for i in range(n):
    visited.add(i)
    dfs(i, 0)
    visited.remove(i)

if flag:
    print(1)
else:
    print(0)