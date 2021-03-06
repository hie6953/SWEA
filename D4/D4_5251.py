# 최소 이동 거리
for tc in range(int(input())):
    N, E = map(int, input().split())
    G = [[] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        G[s].append([e, w])
    q = [0]
    D = [0]+[9999]*N

    for v, w in G[0]:
        D[v] = w
    while len(q) < N+1:
        minV = 9999
        for i in range(N+1):
            if i in q:
                continue
            if minV > D[i]:
                minV = D[i]
                curV = i
        q.append(curV)
        for v, w in G[curV]:
            if v in q:
                continue
            if D[v] > w+D[curV]:
                D[v] = w+D[curV]
    print('#{} {}' .format(tc+1, D[-1]))
