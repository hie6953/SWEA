for tc in range(1, int(input())+1):
    N = int(input())
    people = list(map(int, input().split()))
    avg = sum(people)/N
    cnt = 0
    for p in people:
        if p <= avg:
            cnt += 1
    print('#{}' .format(tc), cnt)