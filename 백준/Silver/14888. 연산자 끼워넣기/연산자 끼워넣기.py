import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
operator_count = list(map(int, sys.stdin.readline().split()))


def recur(index, result):
    global min_result, max_result
    if index == n:
        min_result = min(min_result, result)
        max_result = max(max_result, result)
        return

    #덧셈
    if operator_count[0] > 0:
        operator_count[0] -= 1
        recur(index + 1, result + a[index])
        operator_count[0] += 1
    #뺄셈
    if operator_count[1] > 0:
        operator_count[1] -= 1
        recur(index + 1, result - a[index])
        operator_count[1] += 1
    #곱셈
    if operator_count[2] > 0:
        operator_count[2] -= 1
        recur(index + 1, result * a[index])
        operator_count[2] += 1
    #나눗셈
    if operator_count[3] > 0:
        operator_count[3] -= 1

        recur(index + 1, int(result / a[index]))
        operator_count[3] += 1


min_result = sys.maxsize
max_result = -sys.maxsize

recur(1, a[0])
print(max_result)
print(min_result)