# 최소 신장 트리
def prim():
    u.append(0)
    D[0] = 0
    curV = 0

    for v, w in G[0]:
        D[v] = w

    while len(u) < V + 1:
        minV = 11
        for i in range(V + 1):
            if i in u:
                continue
            if minV > D[i]:
                minV = D[i]
                curV = i
        u.append(curV)

        # 새로 구한 curV(최단거리)로부터의 인접 정점의 거리를 업데이트!
        for v, w in G[curV]:
            if v in u:
                continue
            if D[v] > w:
                D[v] = w
    return sum(D)


for tc in range(int(input())):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        G[n1].append([n2, w])
        G[n2].append([n1, w])
    u = []
    D = [11] * (V+1)
    print('#{} {}' .format(tc+1, prim()))