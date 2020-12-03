for tc in range(int(input())):
    N,L=map(int,input().split())
    info=[list(map(int,input().split())) for _ in range(N)]
    r=info[-1][0]
    for i in range(N-1):
        T=[info[i]]
        for j in range(i+1,N):
            nT=T[:]
            for t1, t2 in nT:
                cal=t2+info[j][1]
                if cal<=L:
                    T.append([t1+info[j][0],cal])
            print('nT', nT)
            print('T', T)
        if r<max(T)[0]:
            r=max(T)[0]
    print('#{} {}' .format(tc+1, r))

'''
1
5 1000
100 200
300 500
250 300
500 1000
400 400
'''