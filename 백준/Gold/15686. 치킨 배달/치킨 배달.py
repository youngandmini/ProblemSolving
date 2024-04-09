import sys
from itertools import combinations

n,m = map(int, sys.stdin.readline().split())

arr = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

houses = []
chickens = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            houses.append((i,j))
        elif arr[i][j] == 2:
            chickens.append((i,j))

def calculate_distance(houses, chicken_comb):
    total_distance = 0
    for house_i, house_j in houses:
        min_distance = sys.maxsize
        for chicken_i, chicken_j in chicken_comb:
            min_distance =  min(min_distance, abs(chicken_i-house_i) + abs(chicken_j-house_j))
        total_distance += min_distance
        
    return  total_distance

answer = sys.maxsize
for comb in combinations(chickens, m):
    answer = min(answer, calculate_distance(houses, comb))
print(answer)