def change_color(N):
    x, y, c = map(int, input().split())
    if c == 1:
        bc = 2
    elif c == 2:
        bc = 1
    tmp[y][x] = c
    for d in range(8):
        newX = x +dx[d]
        newY = y +dy[d]
        while 0<newX<(N+1) and 0<newY<(N+1) and tmp[newY][newX] == bc:
            newX += dx[d]
            newY += dy[d]
        if 0<newX<(N+1) and 0<newY<(N+1) and tmp[newY][newX] == c:
            while x != newX or y != newY:
                newX -= dx[d]
                newY -= dy[d]
                tmp[newY][newX] = c
 
dx = [0, 0, 1, 1, 1, -1, -1, -1]
dy = [1, -1, 0, 1, -1, 0, 1, -1]
 
for idx in range(1, int(input())+1):
    N, M = map(int, input().split())
    tmp = [[0]*(N+2) for _ in range(N+2)]
    tmp[N//2][N//2] = tmp[N//2+1][N//2+1] = 2
    tmp[N//2][N//2+1] = tmp[N//2+1][N//2] = 1
    for m in range(M):
        change_color(N)
    b = w = 0
    for i in range(1, N+1):
        for j in range(1, N+1):
            if tmp[i][j] == 1:
                b += 1
            elif tmp[i][j] == 2:
                w += 1
    print('#{} {} {}' .format(idx, b, w))