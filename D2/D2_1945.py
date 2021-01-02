# 1945. 간단한 소인수분해
for tc in range(int(input())):
    N=int(input())
    I=[2,3,5,7,11]
    C=[0]*5
    i=0
    while i<5:
        if N%I[i]==0:
            N//=I[i]
            C[i]+=1
        else:
            i+=1
    print(f'#{tc+1}', end=' ')
    print(*C)