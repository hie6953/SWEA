for tc in range(int(input())):
    print('#{}' .format(tc+1))
    N=int(input())
    e=0
    for n in range(N):
        s,t=input().split()
        t=int(t)
        while t!=0:
            if e+t>=10:
                print(s*(10-e))
                t-=10-e
                e=0
            else:
                print(s*t, end='')
                e=t
                t=0
    print()