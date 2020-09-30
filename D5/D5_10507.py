for tc in range(1, int(input())+1):
    N, P = map(int, input().split())
    day = list(map(int, input().split()))
    ans = P+1
    r = 1
    for n in range(N):
        while r < N:
            if day[r]-day[n] <= r-n+P:
                ans = max(r-n+P+1, ans)
                r += 1
            else:
                break        
    print('#{} {}' .format(tc, ans))