for tc in range(1, int(input())+1):
    D, H, M = map(int, input().split())
    ans = ((D-11)*24+(H-11))*60+M-11
    if ans<0:
        ans = -1
    print('#{}' .format(tc), ans)