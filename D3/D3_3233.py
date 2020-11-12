# 정삼각형 분할 놀이
for tc in range(int(input())):
    A, B = map(int, input().split())
    # 각 줄은 2n-1, n줄
    # (1+2+3+...+n)*2 - 1*n
    # = n(n+1)//2*2 - n
    # = n**2
    print('#{} {}' .format(tc+1,(A//B)**2))