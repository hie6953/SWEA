# 1959. 두 개의 숫자열
for tc in range(int(input())):
    N,M=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    (L,S,X,Y)=(l1,l2,N,M) if N>M else (l2,l1,M,N)
    r=-1000
    for i in range(X-Y+1):
        t=0
        for j in range(Y):
            t+=L[i+j]*S[j]
        r=max(t,r)
    print('#{} {}' .format(tc+1,r))


for tc in range(int(input())):
    N,M=map(int,input().split())
    l=[list(map(int,input().split())) for _ in range(2)]
    (L,S,X,Y)=(l[0],l[1],N,M) if N>M else (l[1],l[0],M,N)
    r=-1000
    for i in range(X-Y+1):
        t=0
        for j in range(Y):
            t+=L[i+j]*S[j]
        r=max(t,r)
    print('#{} {}' .format(tc+1,r))