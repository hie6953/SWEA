for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    # i는 유니콘 j는 트윈혼
    for i in range(M+1):
        j = M-i
        if i+2*j==N:
            print('#{}' .format(tc), i, j)
            break