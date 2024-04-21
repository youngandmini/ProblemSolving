import sys

n,m = map(int, sys.stdin.readline().split())
books = list(map(int, sys.stdin.readline().split()))

# 갔다가 돌아왔다가를 반복하다가, 마지막에는 돌아오지 않고 종료한다.
# 양수와 음수를 분리해서 고려해야한다.
# 어차피 끝까지 이동해야한다면, 그 이전 위치의 책들도 함께 옮겨주는 것이 좋다.
# -> 그리디

books.sort()
move_distances = []

i = 0
carry = 0 # 현재 옮기고 있는 책 수
move = 0
while i<n and books[i] < 0: #음수일 때
    if carry == 0:
        move_distances.append( -books[i])
    i += 1
    carry = (carry+1) % m

i = n-1
carry = 0
while i>=0 and books[i] > 0: #양수일 때
    if carry == 0:
        move_distances.append(books[i])
    i -= 1
    carry = (carry + 1) % m

move_distances.sort()
print(2*sum(move_distances) - move_distances[-1])