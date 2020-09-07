for tc in range(1, int(input())+1):
    lst = [input() for _ in range(5)]
    max_len = 0
    for l in lst:
        if len(l) > max_len:
            max_len = len(l)
    print('#{} ' .format(tc), end='')
    for i in range(max_len):
        for j in range(5):
            if i>= len(lst[j]):
                continue
            print(lst[j][i], end='')
    print()