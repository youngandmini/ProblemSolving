def solution(clothes):
    clothes_map = {}
    for name, category in clothes:
        clothes_map[category] = clothes_map.get(category, 0) + 1
    
    answer = 1
    for category in clothes_map:
        answer *= clothes_map[category]+1
    return answer-1