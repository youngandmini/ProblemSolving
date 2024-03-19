def solution(n):
    
    dp_table = [0 for i in range(n+1)]
    dp_table[1] = 1
    
    if len(dp_table) >= 3:
        dp_table[2] = 2
    
    for i in range(3, n+1):
        dp_table[i] = (dp_table[i-1] + dp_table[i-2]) % 1234567
    
    return dp_table[n]