import math
def solution(brown, yellow):
    # 연립방정식의 플마 루트 b제곱 - 4ac 부분
    plus_minus = int((math.pow(brown-4, 2)-(16*yellow))**(1/2))
    
    # 노란색의 가로길이
    horizontal = (brown - 4 + plus_minus) // 4
    # 노란색의 세로길이
    vertical = (brown - 4 - plus_minus) // 4
    
    # 노란색 둘레로 테두리가 쳐져있으니 +2씩 해줘야함
    answer = [horizontal+2, vertical+2]
    return answer