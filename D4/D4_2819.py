def dfs(i, j, num):
    if len(num) == 7:
        if num not in check:
            check.append(num)
        return
    for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        ni = i + di
        nj = j + dj
        if 0<=ni<4 and 0<=nj<4:
            dfs(ni, nj, num+lst[ni][nj])


for tc in range(1, int(input())+1):
    lst = [input().split() for _ in range(4)]
    check = []
    for i in range(4):
        for j in range(4):
            dfs(i, j, lst[i][j])
    print('#{} {}' .format(tc, len(check)))