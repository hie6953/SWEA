for tc in range(int(input())):
    W=input()
    t=1
    while True:
        c=0
        T=W[:t]
        for w in range(t,(30//t)*t+1,t):
            n=W[w:w+t]
            if n==T:
                c+=1
            else:
                break
        if c==(30//t-1):
            break
        t+=1
    print('#{} {}' .format(tc+1,t))
