
import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

arr = list(map(int, sys.stdin.readline().split()))
arr.sort()

distance_diff = []
for i in range(n-1):
    distance_diff.append(arr[i+1] - arr[i])

distance_diff.sort()
result = 0

# 가장 간격이 넓은 k-1개는 뺀다.
for i in range(len(distance_diff)-(k-1)):
    result += distance_diff[i]

print(result)