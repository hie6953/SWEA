for tc in range(1, int(input())+1):
    N = int(input())
    lst = sorted(list(map(int, input().split())))
    t = sum(lst)
    I = N//3
    j = N%3
    lst = lst[j:]
    for i in range(0, I):
        t -= lst[i*3]
    print('#{} {}' .format(tc, t))