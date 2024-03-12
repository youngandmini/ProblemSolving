def solution(arr):
    max_number = max(arr)
    
    lcm = max_number
    while True:
        lcm_flag = True
        for num in arr:
            if lcm % num != 0:
                lcm_flag = False
                break
        if lcm_flag:
            return lcm
        else:
            lcm += max_number