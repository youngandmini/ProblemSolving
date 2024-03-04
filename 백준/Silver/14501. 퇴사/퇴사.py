import sys

n = int(sys.stdin.readline())
counsel = []

for i in range(n):
    counsel.append(list(map(int, sys.stdin.readline().split())))

# 범위 고려를 안해도 되도록 넉넉하게 설정
# max(n) + max(t) = 20
money = [0 for i in range(20)]

for i in range(n):
    t, p = counsel[i]
    money[i+1] = max(money[i+1], money[i])
    money[i+t] = max(money[i+t], money[i]+p)

print(money[n])