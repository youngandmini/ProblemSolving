import sys

n = int(sys.stdin.readline())

arr = [(list(map(int, sys.stdin.readline().rstrip().split()))) for i in range(n)]

def recur(index, start, link):
    global n

    if index == n:
        calculate_score(start, link)
        return

    if len(start) < n//2:
        recur(index + 1, start + [index], link)
    if len(link) < n // 2:
        recur(index + 1, start, link+ [index])

def calculate_score(start, link):
    global min_score_diff, n, arr

    start_power = 0
    link_power = 0
    for i in range((n//2) -1):
        for j in range(i+1, n//2):
            start_power += arr[start[i]][start[j]]
            start_power += arr[start[j]][start[i]]
            link_power += arr[link[i]][link[j]]
            link_power += arr[link[j]][link[i]]
    min_score_diff = min(min_score_diff, abs(start_power - link_power))

min_score_diff = sys.maxsize
recur(0, [], [])
print(min_score_diff)