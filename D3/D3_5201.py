for tc in range(int(input())):
    N, M = map(int, input().split())
    wi = sorted(list(map(int, input().split())), reverse=True)
    ti = sorted(list(map(int, input().split())), reverse=True)
    t = i = j = 0
    while i<len(wi) and j<len(ti):
        if wi[i] > ti[j]:
            i += 1
        elif wi[i] <= ti[j]:
            t += wi[i]
            i += 1
            j += 1
    print('#{} {}' .format(tc+1, t))