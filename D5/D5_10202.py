for tc in range(1, int(input())+1):
    n = int(input())
    A = input()
    B = input()
    C = input()
    cnt = 0
    for i in range(n):
        l = set()
        l.add(A[i])
        l.add(B[i])
        l.add(C[i])
        if len(l) == 2:
            cnt += 1
        elif len(l) == 3:
            cnt += 2
    print('#{}' .format(tc), cnt)