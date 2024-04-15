import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

def solve(arr):
    # 하나밖에 없으면 앞으로의 경우의 수는 무수히 많다.
    if len(arr) == 1:
        return "A"
    # 두 수가 주어졌다면
    if len(arr) == 2:
        # 같은 수라면 이후로도 쭉 같은수여야한다.
        if arr[0] == arr[1]:
            return arr[0]
        # 같은 수가 아니라면 가능한 경우의 수는 무수히 많다.
        return "A"

    # 세 개 이상의 수가 주어졌다면
    # a*[현재 수] + b = [다음 수]
    # 연립방정식을 통해 풀자.

    # 세 수가 같다면 이후에도 같아야한다.
    if arr[0] == arr[1] == arr[2]:
        a = 1
        b = 0
    # 첫 두 수가 같은데 세번째 이후로 달라진다면 불가능한 수열
    elif arr[0] == arr[1] != arr[2]:
        return "B"
    else:
        #arr[0] * a + b = arr[1]
        #arr[1] * a + b = arr[2]
        # -> (arr[1] - arr[0])*a = (arr[2] - arr[1])
        # -> a = (arr[2] - arr[1]) / (arr[1] - arr[0])
        # 이때 a가 정수여야만 한다.
        if (arr[2] - arr[1]) % (arr[1] - arr[0]) != 0:
            return "B"
        a = (arr[2] - arr[1]) // (arr[1] - arr[0])
        b = arr[1] - (arr[0]*a)

    # a,b는 주어졌으니 이제 모든 수에 대해서 a, b가 적용되는지 확인
    for i in range(2, len(arr)-1):
        if (arr[i]*a + b) != arr[i+1]:
            return "B"

    # 모든 수에 대해서 a,b가 적용된다면 다음 수를 구함
    return arr[-1] *a + b

print(solve(arr))