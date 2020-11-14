# 그룹 나누기
def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


def union(x, y):
    p[find_set(y)] = find_set(x)


for tc in range(int(input())):
    N, M = map(int, input().split())
    team = list(map(int, input().split()))
    p = [i for i in range(N+1)]
    cnt = 0
    for i in range(M):
        a, b = team[i*2], team[i*2+1]
        union(a, b)
    for j in range(1, N+1):
        if p[j] == j:
            cnt += 1
    print('#{} {}' .format(tc+1, cnt))