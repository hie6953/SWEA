from collections import deque


def cal(n, c):
    Q = deque()
    Q.append((n, c))
    while Q:
        v, c = Q.popleft()
        t = [v+1, v-1, v*2, v-10]
        for i in range(4):
            if 0 < t[i] <= SIZE:
                if t[i] == M:
                    return c+1
                if not vtd[t[i]]:
                    vtd[t[i]] = c+1
                    Q.append((t[i], c+1))


for tc in range(int(input())):
    N, M = map(int, input().split())
    SIZE = max(N, M) + 10
    vtd = [0] * (SIZE + 1)
    print('#{} {}' .format(tc+1, cal(N, 0)))