def solution(k, dungeons):
    answer = -1
    visited_set = set()
    def recur(tired, depth):
        nonlocal answer, visited_set, dungeons
        
        answer = max(answer, depth)
        for i in range(len(dungeons)):
            if i not in visited_set and tired >= dungeons[i][0]:
                visited_set.add(i)
                recur(tired - dungeons[i][1], depth+1)
                visited_set.remove(i)
        
    recur(k, 0)
    return answer