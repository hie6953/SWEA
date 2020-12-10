prime=[2,3,5,7]
lst=list(range(13,533,2))
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
print(*prime,sep=' ')