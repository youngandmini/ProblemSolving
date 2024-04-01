import sys

n = int(sys.stdin.readline())
weights = list(map(int, sys.stdin.readline().split()))

m  = int(sys.stdin.readline())
marbels = list(map(int, sys.stdin.readline().split()))

# 추를 이용해서 모든 측정 가능한 무게를 찾고
# 구슬마다 확인?

# 아니면 구슬마다 되는지 확인?

# 추를 놓는 경우의 수
# 1. 왼쪽에 둔다.
# 2. 오른쪽에 둔다.
# 3. 바닥에 둔다.(저울에 안올린다)

dp_set = {0}

# 다음 추를 고려
for weight in weights:

    next_dp_set = set()
    for total_weight in dp_set:
        # 왼쪽에 둔다. -> 그만큼 무게가 더해진다.
        next_dp_set.add(total_weight + weight)
        # 오른쪽에 둔다. -> 그만큼 무게가 빠진다.
        next_dp_set.add(abs(total_weight - weight))
        # 바닥에 둔다. -> 그대로임

    dp_set = dp_set.union(next_dp_set)

for marbel in marbels:
    if marbel in dp_set:
        print("Y", end = " ")
    else:
        print("N", end = " ")