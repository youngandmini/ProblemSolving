def solution(want, number, discount):
    
    want_dict = {}
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
    
    discount_dict = {}
    for i in range(10):
        discount_dict[discount[i]] = discount_dict.get(discount[i], 0) +1
    
    count = 0
    if discount_dict == want_dict:
        count += 1
    
    for index in range(len(discount)-10):
        
        discount_dict[discount[index+10]] = discount_dict.get(discount[index+10], 0) +1
        discount_dict[discount[index]] = discount_dict[discount[index]] - 1
        if discount_dict[discount[index]] <= 0:
            discount_dict.pop(discount[index])
        
        if discount_dict == want_dict:
            count += 1
    
    return count