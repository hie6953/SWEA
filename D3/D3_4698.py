prime=[2,3,5,7]
lst=list(range(11,999999,2))
n=1
for i in lst:
    check=1
    if i>prime[n]**2:
        n+=1
    for p in prime[1:n+1]:
        if i%p==0:
            check=0
            break
    if check:
        prime.append(i)
for tc in range(int(input())):
    D, A, B = map(int, input().split())
    D=str(D)
    t = 0
    for p in prime:
        if p>B:
            break
        if p>=A:
            if D in str(p):
                t+=1
    print(f'#{tc+1} {t}')