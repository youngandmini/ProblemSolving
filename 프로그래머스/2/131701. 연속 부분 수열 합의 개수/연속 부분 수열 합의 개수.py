def solution(elements):
    elements_len = len(elements)
    
    elements = elements + elements[:-1]
    print(elements)
    
    part_sum_set = set()
    
    # 길이가 length인 부분수열을 만드는데
    for length in range(1, elements_len+1):
        part_sum = sum(elements[:length])
        part_sum_set.add(part_sum)
        
        for i in range(elements_len-1):
            part_sum -= elements[i]
            part_sum += elements[i+length]
            part_sum_set.add(part_sum)
            
    return len(part_sum_set)