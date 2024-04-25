import sys
import heapq

n,k = map(int, sys.stdin.readline().split())

# 가장 가격이 비싼 보석을 가장 핏한 가방에 집어넣는다?
# 핏한 가방을 찾으려면? 완전탐색하면 시간초과 각인데... 이분탐색?
# 아니면 작은 가방부터 채운다?

jewels = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
heapq.heapify(jewels)

bags = [int(sys.stdin.readline()) for i in range(k)]
bags.sort()

total_price = 0
hq = []
for weight in bags:
    while jewels and jewels[0][0] <= weight:
        jewel = heapq.heappop(jewels)
        heapq.heappush(hq, -jewel[1])
    if hq:
        total_price -= heapq.heappop(hq)

print(total_price)