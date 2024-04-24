def dp(dp_table, triangle, height, width):
    if height == 0:
        return dp_table[0][0]
    
    if width < 0 or width > height:
        return -1
    
    if dp_table[height][width] == -1:
        dp_table[height][width] = triangle[height][width] + max(dp(dp_table, triangle, height-1, width-1), dp(dp_table, triangle, height-1, width))
        
    return dp_table[height][width]

def solution(triangle):
    dp_table = [[-1 for j in range(i+1)] for i in range(len(triangle))]
    dp_table[0][0] = triangle[0][0]
    
    for width in range(len(triangle)):
        dp(dp_table, triangle, len(triangle) - 1, width)
        
    answer = 0
    return max(dp_table[-1])