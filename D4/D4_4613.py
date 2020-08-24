for idx in range(1, int(input())+1):
    N, M = map(int, input().split())
    #붙어서 들어오는 문자열 받기
    lst = [input() for _ in range(N)]
    # 붙으서 들어오는 문자열 띄어서 받기
    # lst = [list(input()) for _ in range(N)]
    # 위에 2개다 lst[1][1] 2차열배열로 불러올 수 있음
    W = [0]*N
    B = [0]*N
    R = [0]*N
    # 전체에서 해당 색깔을 뺀 값
    for i in range(N):
        W[i] = M - lst[i].count('W')
        B[i] = M - lst[i].count('B')
        R[i] = M - lst[i].count('R')
    t_min = N*M
    for i in range(N-2):
        tW = 0
        for w in range(0, i+1):
            tW += W[w]
        for j in range(i+1, N-1):
            tB = 0
            for b in range(i+1, j+1):
                tB += B[b]
            for k in range(j+1, N):
                tR = 0
                for r in range(j+1, k+1):
                    tR += R[r]
            if t_min > tW + tB + tR:
                t_min = tW + tB + tR
    print('#{} {}' .format(idx, t_min))

        


# for i : 0 > N-3
#     for j: i+1 > N-2
#         s1 = W[i]
#         s2 = B[j]-B[i]
#         s3 = R[N-1] - R[j]
#         if minV > s1+s2+s3
#             minV = s1 + s2 + s3