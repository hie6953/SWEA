for idx in range(1, int(input())+1):
    N, M = map(int, input().split())
    pizza = list(map(int, input().split()))
    Q = []
    now = []
    for i in range(N):
        Q.append(pizza[i])
        now.append(i)
    while len(now) != 1:
        p = Q.pop(0)
        n = now.pop(0)
        p //= 2
        if p != 0:
            Q.append(p)
            now.append(n)
        else:
            i += 1
            if i<M:
                Q.append(pizza[i])
                now.append(i)
    print('#{} {}' .format(idx, now.pop()+1))
