def solution(m, n, puddles):
    
    arr = [[0 for j in range(m)] for i in range(n)]
    
    for j,i in puddles:
        arr[i-1][j-1] = -1
    
    for j in range(m):
        if arr[0][j] == -1:
            break
        arr[0][j] = 1
    for i in range(n):
        if arr[i][0] == -1:
            break
        arr[i][0] = 1
    
    for i in range(1, n):
        for j in range(1, m):
            if arr[i][j] == -1:
                continue
            
            left = max(arr[i][j-1], 0)
            up = max(arr[i-1][j], 0)
            
            arr[i][j] = (left + up) % 1000000007

    return arr[n-1][m-1]