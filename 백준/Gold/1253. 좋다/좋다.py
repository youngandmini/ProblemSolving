import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

sum_set = set()

if n == 1:
    print(0)
    exit(0)

# "다른" 두 수를 더해서 해당 수가 돼어야함
# -> 0이 포함되어 있을 경우에, 같은 수가 두번은 나와야한다.
# -> 0은 3번이 나와야 0을 표현할 수 있다.

frequency_dict = {}

for i in range(n):
    frequency_dict[arr[i]] = frequency_dict.get(arr[i], 0) + 1
    for j in range(i+1, n):
        if arr[i] != 0 and arr[j] != 0:
            sum_set.add(arr[i] + arr[j])

if frequency_dict.get(0, 0) > 0:
    for key in frequency_dict:
        if key != 0 and frequency_dict[key] >= 2:
            sum_set.add(key)
    if frequency_dict[0] >= 3:
        sum_set.add(0)

count = 0
for num in arr:
    if num in sum_set:
        count += 1
print(count)