def distance(i, d1, d2, d):
    global minD
    if d > minD:
        return
    if i == N:
        d += abs(d1-lst[2])+abs(d2-lst[3])
        if d < minD:
            minD = d
        return
    else:
        for j in range(N):
            if vtd[j] == 0:
                vtd[j] = 1
                distance(i+1, custom[2*j], custom[2*j+1], d+abs(d1-custom[2*j])+abs(d2-custom[2*j+1]))
                vtd[j] = 0


for tc in range(int(input())):
    N = int(input())
    lst = list(map(int, input().split()))
    custom = lst[4:]
    vtd = [0]*N
    minD = 200*N
    distance(0, lst[0], lst[1], 0)
    print('#{} {}' .format(tc+1, minD))