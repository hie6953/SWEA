num = [13, 25, 19, 61, 35, 49, 47, 59, 55, 11]
for tc in range(int(input())):
    N, M = map(int, input().split())
    code = [input() for _ in range(N)]
    for c in code:
        if c != '0'*M:
            break
    for i in range(M-1,-1,-1):
        if c[i] == '1':
            break
    lst = []
    for j in range(8):
        for k in range(10):
            if num[k] == int(c[i-55+j*7:i-48+j*7], 2):
                lst.append(k)
    t = 0
    for l in range(8):
        t+= lst[l] if l%2 else lst[l]*3
    r = 0 if t%10 else sum(lst)
    print(f'#{tc+1} {r}')