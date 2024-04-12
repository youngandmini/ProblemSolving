import sys
from itertools import permutations

strings = [sys.stdin.readline().rstrip() for i in range(6)]

# 6개 순서 정하는 경우의 수 -> 6*5*4*3*2*1 = 720개

index_permutaions = list(permutations(range(6)))

for index in index_permutaions:
    r0 = strings[index[0]]
    r1 = strings[index[1]]
    r2 = strings[index[2]]
    c0 = strings[index[3]]
    c1 = strings[index[4]]
    c2 = strings[index[5]]

    if r0[0]+r1[0]+r2[0] == c0:
        if r0[1] + r1[1] + r2[1] == c1:
            if r0[2] + r1[2] + r2[2] == c2:
                print(r0,r1,r2, sep="\n")
                break
else:
    print(0)
