for tc in range(1, 11):
    N = int(input())
    lst = list(map(int, input().split()))
    i = 2
    t = 0
    while i < N-2:
        if lst[i] == max(lst[i-2:i+3]):
            t += lst[i] - max(lst[i-2:i]+lst[i+1:i+3])
            i += 3
        else:
            i += 1
    print('#{} {}' .format(tc, t))