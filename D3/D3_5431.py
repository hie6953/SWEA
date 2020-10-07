for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    submit = sorted(list(map(int, input().split())))
    print('#{}' .format(tc), end=' ')
    i = 0
    for n in range(1, N+1):
        if i<K and n == submit[i]:
            i += 1
        else:
            print(n, end=' ')
    print()