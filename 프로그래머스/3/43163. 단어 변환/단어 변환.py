from collections import deque

def check(from_str, to_str):
    count = 0
    for i in range(len(from_str)):
        if from_str[i] != to_str[i]:
            count += 1
    if count == 1:
        return True
    else:
        return False

def solution(begin, target, words):
    dq = deque()
    visited = set()
    
    # (word, depth)
    dq.append((begin, 0))
    
    while dq:
        current_word, current_depth = dq.popleft()
        if current_word == target:
            return current_depth
        for next_word in words:
            if next_word not in visited and check(current_word, next_word):
                visited.add(next_word)
                dq.append((next_word, current_depth+1))
    
    return 0