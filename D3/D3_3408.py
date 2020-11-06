# 3408. 세가지 합 구하기
for t in range(int(input())):
    N=int(input())
    n=N**2
    print('#{} {} {} {}' .format(t+1,(n+N)//2,n,n+N))