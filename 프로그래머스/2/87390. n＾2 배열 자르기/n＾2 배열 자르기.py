def solution(n, left, right):
    
    answer = []
    for number in range(left, right+1):
        i = number // n
        j = number % n
        answer.append(max(i,j)+1)
    
    return answer