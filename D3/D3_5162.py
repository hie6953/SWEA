for tc in range(1, int(input())+1):
    A, B, C = map(int, input().split())
    print('#{}' .format(tc), C//min(A, B))