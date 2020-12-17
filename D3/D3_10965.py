prime=[2]
for i in range(3,3162,2):
    for p in prime:
        if i%p==0:break
    else:prime.append(i)
ans=[]
for tc in range(int(input())):
    N=int(input())
    n,r=N,1
    if N**0.5!=int(N**0.5):
        for p in prime:
            m=0
            while n%p==0:
                n//=p
                m+=1
            if m%2:
                r*=p
            if n==1 or p>N:
                break
        if n>1:
            r*=n
    ans.append('#{} {}' .format(tc+1,r))
for a in ans:
    print(a)