import sys

# 해당 위치로 이동할 수 있는가
def moveable(row, col):
    global arr
    if 0<=row<8 and 0<=col<8:
        return True
    else:
        return False

king_position, stone_position, n = sys.stdin.readline().rstrip().split()
n = int(n)

column_serializer = {'A': 0,'B': 1,'C': 2,'D': 3,'E': 4,'F': 5,'G': 6,'H': 7}
column_deserializer = {0:'A',1:'B',2:'C',3:'D',4:'E',5:'F',6:'G',7:'H'}
row_serializer = {'8': 0,'7': 1,'6': 2,'5': 3,'4': 4,'3': 5,'2': 6,'1': 7}
row_deserializer = {0:'8',1:'7',2:'6',3:'5',4:'4',5:'3',6:'2',7:'1'}

command_row_mapper = {'R':0,'L':0,'B':1,'T':-1,'RT':-1,'LT':-1,'RB':1,'LB':1}
command_column_mapper = {'R':1,'L':-1,'B':0,'T':0,'RT':1,'LT':-1,'RB':1,'LB':-1}

king_row = row_serializer[king_position[1]]
king_col = column_serializer[king_position[0]]
stone_row = row_serializer[stone_position[1]]
stone_col = column_serializer[stone_position[0]]

for rep in range(n):
    command = sys.stdin.readline().rstrip()
    row_move = command_row_mapper[command]
    col_move = command_column_mapper[command]

    next_king_row = king_row + row_move
    next_king_col = king_col + col_move

    if next_king_row==stone_row and next_king_col==stone_col:
        next_stone_row = next_king_row + row_move
        next_stone_col = next_king_col + col_move
        if moveable(next_stone_row, next_stone_col):
            stone_row=next_stone_row
            stone_col = next_stone_col
            king_row = next_king_row
            king_col = next_king_col
    elif moveable(next_king_row, next_king_col):
        king_row = next_king_row
        king_col = next_king_col

print(column_deserializer[king_col], row_deserializer[king_row], sep="")
print(column_deserializer[stone_col], row_deserializer[stone_row], sep="")