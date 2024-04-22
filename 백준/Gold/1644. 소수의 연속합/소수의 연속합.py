import sys
import math
from collections import deque
# 2는 처음부터 넣을 거니까 2는 판정하지 않는다고 가정
def get_next_prime_number(k):
    next_num = k+1
    while True:
        if next_num % 2 == 0:
            next_num += 1
            continue

        for divider in range(2, int(math.sqrt(next_num))+1):
            if next_num % divider == 0:
                next_num += 1
                break
        else:
            return  next_num

n = int(sys.stdin.readline())


prime_number_dq =deque([2])
prime_number_sum = 2

if n == 1:
    print(0)
    exit(0)

count =0
while True:
    if prime_number_sum > n:
        prime_number_sum -=prime_number_dq.popleft()
        continue

    if prime_number_sum == n:
        count += 1

    next_prime_number = get_next_prime_number(prime_number_dq[-1])
    if next_prime_number > n:
        break
    prime_number_dq.append(next_prime_number)
    prime_number_sum += next_prime_number

print(count)