# 시간초과
import sys

# 최종 결과물이 이렇게 되어야함
target_arr = [[0 for j in range(3)] for i in range(6)]

def recur(team1, team2):
    global arr, flag, target_arr

    if flag == True:
        return

    if team2 == 6:
        team1 += 1
        team2 = team1 + 1

    if team1 == 5:
        if arr == target_arr:
            flag = True
        return

		# team1 승리
    if arr[team1][0] > 0 and arr[team2][2] > 0:
        arr[team1][0] -= 1
        arr[team2][2] -= 1
        recur(team1, team2+1)
        arr[team1][0] += 1
        arr[team2][2] += 1

    # team1 무승부
    if arr[team1][1] > 0 and arr[team2][1] > 0:
        arr[team1][1] -= 1
        arr[team2][1] -= 1
        recur(team1, team2 + 1)
        arr[team1][1] += 1
        arr[team2][1] += 1

    # team1 패배
    if arr[team1][2] > 0 and arr[team2][0] > 0:
        arr[team1][2] -= 1
        arr[team2][0] -= 1
        recur(team1, team2 + 1)
        arr[team1][2] += 1
        arr[team2][0] += 1

def wdl_checker(arr):
    for w,d,l in arr:
        if w+d+l != 5:
            return False
    return True

result = []
for i in range(4):
    wa, da, la, wb, db, lb, wc, dc, lc,wd, dd, ld, we, de, le, wf, df, lf = map(int, sys.stdin.readline().split())
    arr = [[wa, da, la], [wb, db, lb], [wc, dc, lc],[wd, dd, ld], [we, de, le], [wf, df, lf]]

    if not wdl_checker(arr):
        result.append(0)
        continue

    flag = False
    recur(0, 1)

    if flag:
        result.append(1)
    else:
        result.append(0)
print(*result)