def dfs(v):
    vtd[v] = 1
    for w in lst[v]:
        if vtd[w] == 0:
            dfs(w)


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    lst = [[] for _ in range(N+1)]
    vtd = [0]*(N+1)
    cnt = 0
    for _ in range(M):
        n1, n2 = map(int, input().split())
        lst[n1].append(n2)
        lst[n2].append(n1)
    for v in range(1, N+1):
        if vtd[v] == 0:
            cnt += 1
            dfs(v)
    print('#{} {}' .format(tc, cnt))