import sys

n,r,c = map(int, sys.stdin.readline().split())


def divide_by_4(m, i, j, count):

    if m==2:
        if i==0:
            if j==0:
                print(count)
                return
            else:
                print(count+1)
                return
        else:
            if j==0:
                print(count+2)
                return
            else:
                print(count+3)
                return

    if i < m//2:
        if j < m//2:
            divide_by_4(m//2, i, j, count)
        else:
            divide_by_4(m // 2, i, j-m//2, count + (m // 2)**2)
    else:
        if j < m//2:
            divide_by_4(m//2, i-m//2, j, count+ (m**2)//2)
        else:
            divide_by_4(m // 2, i-m//2, j - m // 2, count + (m**2)//2 + (m // 2)**2)


divide_by_4(2**n, r, c, 0)