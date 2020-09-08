def f(i, j, t):
    global minV
    if i == j == N-1:
        t += lst[i][j]
        if minV > t:
            minV = t
        return
    for di, dj in [(1, 0), (0, 1)]:
        ni, nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<N and t+lst[i][j] < minV:
            f(ni, nj, t+lst[i][j])


for tc in range(1, int(input())+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    minV = 10*N*N
    f(0, 0, 0)
    print('#{} {}' .format(tc, minV))