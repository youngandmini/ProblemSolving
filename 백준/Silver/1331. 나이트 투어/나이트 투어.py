
#1

def validate_movement(recent_row, recent_column, current_row, current_column):
    if abs(recent_row - current_row) == 1:
        if abs(recent_column - current_column) == 2:
            return True
    elif abs(recent_row - current_row) == 2:
        if abs(recent_column - current_column) == 1:
            return True
    return False

import sys

alphabet_mapper = {"A":0, "B":1, "C":2, "D":3, "E":4, "F":5}

first_position = sys.stdin.readline().rstrip()
visited = {first_position}
first_row = int(first_position[1])
first_column = alphabet_mapper[first_position[0]]

current_row = first_row
current_column = first_column

for rep in range(35):
    recent_row = current_row
    recent_column = current_column

    current_position = sys.stdin.readline().rstrip()
    # 이미 방문했던 곳인가?
    if current_position in visited:
        print("Invalid")
        break
    visited.add(current_position)

    # 이동을 정상적으로 했는가?
    current_row = int(current_position[1])
    current_column = alphabet_mapper[current_position[0]]
    if not validate_movement(recent_row, recent_column, current_row, current_column):
        print("Invalid")
        break
else:
    if validate_movement(current_row, current_column, first_row, first_column):
        print("Valid")
    else:
        print("Invalid")