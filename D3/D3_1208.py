for tc in range(1, 11):
    N = int(input())
    lst = sorted(list(map(int, input().split())))
    for i in range(N):
        lst[0] += 1
        lst[-1] -= 1
        lst = sorted(lst)
    print('#{} {}' .format(tc, lst[-1]-lst[0]))