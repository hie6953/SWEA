for tc in range(int(input())):
    N = int(input())
    bus = [list(map(int, input().split())) for _ in range(N)]
    P = int(input())
    print('#{}' .format(tc+1), end=' ')
    for p in range(P):
        t = 0
        p = int(input())
        for b in bus:
            if b[0]<=p<=b[1]:
                t+=1
        print(t, end=' ')
    print()