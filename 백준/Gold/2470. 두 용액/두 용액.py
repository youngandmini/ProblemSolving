import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

arr.sort()

min_feature = sys.maxsize
min_front = 0
min_rear = n-1

front = 0
rear = n-1

while front < rear:
    if min_feature > abs(arr[front] + arr[rear]):
        min_feature = abs(arr[front] + arr[rear])
        min_front = front
        min_rear = rear

    if arr[front] + arr[rear] == 0:
        break

    elif arr[front] + arr[rear] > 0:
        rear -= 1
    else:
        front += 1

print(arr[min_front], arr[min_rear])