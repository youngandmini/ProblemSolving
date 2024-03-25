import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())

dq = deque()
visited = set()

def check_next_location(next_location, visited):
    if not (0 <= now_location <= 100000):
        return False
    if next_location in visited:
        return False
    return True

found = False
found_jump = 0

dp_map = {}
dq.append((n, 0))
visited.add(n)

while dq:
    now_location, now_jump = dq.popleft()

    if found and found_jump != now_jump:
        break

    #방문 표시
    visited.add(now_location)
    #여기까지 갈 수 있는 경우의 수 업데이트
    dp_map[now_location] = dp_map.get(now_location, 0) +1

    if now_location == k:
        found = True
        found_jump = now_jump
        continue

    if check_next_location(now_location+1, visited):
        dq.append((now_location+1, now_jump +1))

    if check_next_location(now_location-1, visited):
        dq.append((now_location-1, now_jump +1))

    if check_next_location(now_location*2, visited):
        dq.append((now_location*2, now_jump +1))

print(found_jump)
print(dp_map[k])
