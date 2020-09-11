def inord(T):
    if T:
        inord(int(tree[T][2]))
        print(tree[T][1], end='')
        inord(int(tree[T][3]))


for tc in range(1, 11):
    N = int(input())
    tree = [[0]*4] + [list(input().split()) for _ in range(N)]
    for t in tree:
        while len(t) < 4:
            t.append(0)
    print('#{}' .format(tc), end=' ')
    inord(1)
    print()