def find_max(r, s):
    global max_p
    if r == N:
        if max_p < s:
            max_p = s
        return
    else:
        for i in range(N):
            if visit[i] == 0:
                visit[i] = 1
                if max_p < s * p[r][i]:
                    find_max(r + 1, s * p[r][i])
                visit[i] = 0
        return
 
 
T = int(input())
 
for tc in range(1, T + 1):
    N = int(input())
    p = [[i * 0.01 for i in map(int, input().split())] for _ in range(N)]
    max_p = 0
    visit = [0] * N
    find_max(0, 1)
    print('#{} {}' .format(tc, max_p * 100:.6f))