# 1230. [S/W 문제해결 기본] 8일차 - 암호문3
for tc in range(1,11):
    N=input()
    M=list(input().split())
    X=int(input())
    Y=input().split()
    i=c=0
    while c<X:
        if Y[i]=='I':
            x,y=int(Y[i+1]),int(Y[i+2])
            M=M[:x]+Y[i+3:i+3+y]+M[x:]
            i+=3+y
        elif Y[i]=='A':
            y=int(Y[i+1])
            M=M+Y[i+2:i+2+y]
            i+=2+y
        else:
            x,y=int(Y[i+1]),int(Y[i+2])
            M=M[:x]+M[x+y:]
            i+=3
        c+=1
    print('#{}' .format(tc),end=' ')
    print(*M[:10])
    