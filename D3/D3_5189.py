def f(n, t, c):
    global minV
    if c == N:
        t += area[n][0]
        if minV > t:
            minV = t
    if vtd[n] == 0:
        vtd[n] = 1
        for i in range(1, N):
            if vtd[i] == 0:
                f(i, t+area[n][i], c+1)
                vtd[i] = 0


for tc in range(int(input())):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    vtd = [0] * N
    minV = 1000
    f(0, 0, 1)
    print('#{} {}' .format(tc+1, minV))