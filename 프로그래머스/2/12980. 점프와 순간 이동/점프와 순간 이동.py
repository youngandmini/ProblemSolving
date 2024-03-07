def solution(n):
    
    #거꾸로 탐색할 것임
    #짝수면 무조건 아이언맨이 이득
    #홀수면 1칸 이동하고 다시 아이언맨 
    ans = 0
    
    while n >= 1:
        #짝수면
        if n%2 == 0:
            n //= 2
        else:
            n -= 1
            ans += 1

    return ans