for c in range(int(input())):
    N=int(input())
    lst=[int(input()) for _ in range(N)]
    avg=sum(lst)//N
    t=0
    for l in lst:
        t+=abs(avg-l)
    print(f'#{c+1} {t//2}')