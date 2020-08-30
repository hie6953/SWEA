def dfs(n):
    stack.append(n)
    while len(stack) != 0:
        v = stack.pop()
        if v == 99:
            return 1
        if v not in visited:
            visited.append(v)
            if ch1[v] != 0:
                stack.append(ch1[v])
            if ch2[v] != 0:
                stack.append(ch2[v])
    return 0


for _ in range(10):
    N, M = map(int, input().split())
    tmp = list(map(int, input().split()))
    ch1 = [0]*100
    ch2 = [0]*100
    for i in range(M):
        n1 = tmp[i*2]
        n2 = tmp[i*2+1]
        if ch1[n1] == 0:
            ch1[n1] = n2
        else:
            ch2[n1] = n2
    stack = []
    visited = []
    print('#{} {}' .format(N, dfs(0)))