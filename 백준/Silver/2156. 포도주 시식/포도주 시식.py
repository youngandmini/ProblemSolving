"""
i번째 잔을 안먹으려면?
dp_table[i] = ?
i-1번째에 안먹거나,
dp_table[i] = dp_table[i-1][1]
i-2번째에 안먹거나,
dp_table[i] = dp_table[i-2][1]+arr[i-1]
i-3번째에 안먹거나,
dp_table[i] = dp_table[i-3][1]+arr[i-2]+arr[i-1]

i번째 잔을 안먹었을 때의 최댓값은?
dp_table[i] = max(dp_table[i-1], dp_table[i-2]+arr[i-1], dp_table[i-3]+arr[i-2]+arr[i-1])

=> dp_table[i+3] = max(dp_table[i+2], dp_table[i+1]+arr[i+2], dp_table[i]+arr[i+1]+arr[i+2])

전체의 최댓값을 구하려면? 0~n-1번 인덱스까지를 구하고, n번째를 안먹었을 때의 최댓값을 구하자
"""

import sys

n = int(sys.stdin.readline())

arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline()))


dp_table = [0 for i in range(n+1)]

#dp_table을 해당 순서 안먹었을 때의 최댓값이라고 하자.
dp_table[0] = 0
if n>=1:
    dp_table[1] = arr[0]
if n>=2:
    dp_table[2] = arr[0] + arr[1]


for i in range(n-2):
    dp_table[i+3] = max(dp_table[i+2], dp_table[i+1]+arr[i+2], dp_table[i]+arr[i+1]+arr[i+2])

    # print("dp_table[", i+3 ,"] = ", dp_table[i+3], sep="")

# print(dp_table)
print(dp_table[n])
