# 최소 비용
def a():
    Q = []
    darr[0][0] = 0
    Q.append((0, 0))

    while Q:
        curX, curY = Q.pop(0)
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            tx = curX + dx
            ty = curY + dy
            if 0 <= tx < N and 0 <= ty < N:
                dis = max(arr[ty][tx] - arr[curY][curX], 0) + 1
                if darr[curY][curX] + dis < darr[ty][tx]:
                    Q.append((tx, ty))
                    darr[ty][tx] = min(darr[ty][tx], darr[curY][curX] + dis)
    return darr[N-1][N-1]


for tc in range(int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    darr = [[1000000]*(N+1) for _ in range(N+1)]
    print('#{} {}' .format(tc+1, a()))