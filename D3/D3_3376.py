# 3376. 파도반 수열
P=[0,1,1,1,2,2]
for tc in range(int(input())):
    N=int(input())
    r=0
    while r==0:
        lp=len(P)
        if lp > N:
            r=P[N]
        else:
            P.append(P[lp-1]+P[lp-5])
    print('#{} {}' .format(tc+1,r))
