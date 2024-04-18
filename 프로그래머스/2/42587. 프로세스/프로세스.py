from collections import deque
import heapq

def solution(priorities, location):
    target = location
    dq = deque()
    hq = []
    
    for i in range(len(priorities)):
        heapq.heappush(hq, -1 * priorities[i])
        dq.append((-priorities[i], i))
    
    count = 0
    while dq:
        priority, index = dq.popleft()
        if priority == hq[0]:
            heapq.heappop(hq)
            count += 1
            if index == target:
                return count
        else:
            dq.append((priority, index))
