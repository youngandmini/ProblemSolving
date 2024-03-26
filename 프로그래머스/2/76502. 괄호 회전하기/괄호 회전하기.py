def check_valid(s_prime):
    stack = []
    
    for braket in s_prime:
        if braket in ('(','{','['):
            stack.append(braket)
        else:
            if not stack:
                return False
            open_braket = stack.pop()
            if braket == ')' and open_braket != '(':
                return False
            if braket == '}' and open_braket != '{':
                return False
            if braket == ']' and open_braket != '[':
                return False
    if stack:
        return False
    return True

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        s_prime = s[i:] + s[:i]
        if check_valid(s_prime):
            answer += 1
    
    return answer