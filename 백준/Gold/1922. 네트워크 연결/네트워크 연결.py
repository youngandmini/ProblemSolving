import sys
import heapq

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

graph = [[] for i in range(n+1)]

for repeat in range(m):
    a,b, price = map(int, sys.stdin.readline().split())
    graph[a].append((price, b))
    graph[b].append((price, a))

connected = {1}
hq = []
total_price = 0

# 시작점은 1로 잡음
for next_price, next_node in graph[1]:
    heapq.heappush(hq, (next_price, next_node))

while hq:
    price, node = heapq.heappop(hq)
    if node in connected:
        continue
    total_price += price
    connected.add(node)

    for next_price, next_node in graph[node]:
        if next_node not in connected:
            heapq.heappush(hq, (next_price, next_node))

print(total_price)