def solution(citations):
    
    citations.sort()
    
    for i in range(len(citations), 0, -1):
        if citations[len(citations) - i] >= i:
            return i
        
    return 0