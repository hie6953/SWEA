# total에서 빼보면서 진행
def f(n, t):
    global min_t
    if n == N:
        if B<= t < min_t:
            min_t = t
        return
    if B <= t:
        f(n+1, t-lst[n])
        f(n+1, t)


for tc in range(1, int(input())+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    t = sum(lst)
    min_t = t
    f(0, t)
    print('#{} {}' .format(tc, min_t-B))