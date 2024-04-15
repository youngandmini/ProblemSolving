import sys

n1,n2 = map(int, sys.stdin.readline().split())

ants1 = list(sys.stdin.readline().rstrip())
ants2 = list(sys.stdin.readline().rstrip())

ants1.reverse()
ants = ants1 + ants2
ants1_set = set(ants1)
ants2_set = set(ants2)

t = int(sys.stdin.readline())

for repeat in range(t):
    for i in range(n1+n2-1):
        if ants[i] in ants1_set and ants[i+1] in ants2_set:
            ants[i], ants[i+1] = ants[i+1], ants[i]

                        # 처음 개미가 swap한 다음, 계속해서 swap되지 않도록
            if  ants[i+1] == ants1[-1]:
                break
print("".join(ants))