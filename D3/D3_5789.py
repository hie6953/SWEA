for tc in range(1, int(input())+1):
    N, Q = map(int, input().split())
    box = [0]*N
    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            box[j] = i+1
    print('#{}' .format(tc), end=' ')
    for b in box:
        print(b, end=' ')
    print()