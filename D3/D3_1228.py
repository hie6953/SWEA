# 1228. [S/W 문제해결 기본] 8일차 - 암호문1
for tc in range(1,11):
    input()
    M=list(input().split())
    X=int(input())
    Y=input().split()
    i=c=0
    while c<X:
        x,y=int(Y[i+1]),int(Y[i+2])
        s=Y[i+3:i+3+y]
        M=M[:x]+s+M[x:]
        i+=3+y
        c+=1
    print('#{}' .format(tc),end=' ')
    print(*M[:10])