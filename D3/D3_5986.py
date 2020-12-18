# 5986. 새샘이의 세 소수
# 999이하 소수 구하기
prime=[]
for i in range(3,992,2):
    for p in prime:
        if i%p==0:break
    else:
        prime.append(i)
for tc in range(int(input())):
    N=int(input())
    c=0
    # N이 홀수일때 > 4+홀수 or 홀수+홀수+홀수
    if N%2:
        if N-4 in prime:
            c+=1
        for i in range(166):
            if prime[i]>N:break
            ni=N-prime[i]
            for j in range(i,166):
                if prime[j]>ni:break
                nj=ni-prime[j]
                for k in range(j,166):
                    if prime[k]>nj:break
                    if nj-prime[k]==0:
                        c+=1
                        break
    # N이 짝수일때 > 2+홀수+홀수
    else:
        N-=2
        for p in prime:
            i=0
            n=N-p
            while prime[i]<=n:
                if prime[i]==n:
                    c+=1
                i+=1
    print('#{} {}' .format(tc+1,c))