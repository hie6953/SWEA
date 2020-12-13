for tc in range(int(input())):
    N=int(input())
    c=list(map(str,range(10)))
    x=0
    while c:
        x+=1
        K=str(x*N)
        for k in K:
            if k in c:
                c.remove(k)
    print('#{} {}' .format(tc+1,x*N))
