def bfs(i, j):
    cnt = 0
    min_n = lst[i][j]
    Q = []
    Q.append((i, j))
    while Q:
        i, j = Q.pop(0)
        vtd[i][j] = 1
        cnt += 1
        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ni = i + di
            nj = j + dj
            if 0<=ni<N and 0<=nj<N and vtd[ni][nj] == 0 and abs(lst[i][j] - lst[ni][nj]) == 1:
                Q.append((ni, nj))
                if min_n > lst[ni][nj]:
                    min_n = lst[ni][nj]
    global total
    global min_num
    if cnt > total:
        total = cnt
        min_num = min_n
    if cnt == total and min_num > min_n:
        min_num = min_n


for tc in range(1, int(input())+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    vtd = [[0]*N for _ in range(N)]
    total = 1
    min_num = N*N
    for i in range(N):
        for j in range(N):
            if vtd[i][j] == 0:
                bfs(i, j)

    print('#{} {} {}' .format(tc, min_num, total))