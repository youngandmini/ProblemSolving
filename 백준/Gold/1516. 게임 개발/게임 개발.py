import sys

n = int(sys.stdin.readline())

build_cost_map = {}
build_require_map = {}
builded_map = {}

for i in range(n):
    building_num = i+1
    input_list = list(map(int, sys.stdin.readline().split()))

    build_cost_map[building_num] = input_list[0]
    builded_map[building_num] = False

    index = 1
    while input_list[index] != -1:
        require_buildings = build_require_map.get(building_num, set())
        require_buildings.add(input_list[index])
        build_require_map[building_num] = require_buildings
        index += 1

total_cost = [-1 for i in range(n+1)]

def get_build_cost(building_num):

    global builded_map, total_cost

    if total_cost[building_num] != -1:
        return  total_cost[building_num]
    else:
        cost = 0
        for require_building in build_require_map.get(building_num, set()):
            cost = max(cost, get_build_cost(require_building))

        total_cost[building_num] = cost + build_cost_map[building_num]
        return total_cost[building_num]

for building in range(1, n+1):
    get_build_cost(building)

for i in range(1, n+1):
    print(total_cost[i])