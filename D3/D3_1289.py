for tc in range(1, int(input())+1):
    M = input()
    s = '0'
    cnt = 0
    for m in M:
        if m != s:
            cnt += 1
            s = m
    print('#{} {}' .format(tc, cnt))