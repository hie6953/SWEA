#1
M = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for tc in range(1, int(input())+1):
    D = 3
    m, d = map(int, input().split())
    D+= sum(M[:m])+d
    print('#{}' .format(tc), D%7)

#2
M = [3, 3, 1, 3, 2, 3, 2, 3, 3, 2, 3, 2, 0]
for tc in range(1, int(input())+1):
    m, d = map(int, input().split())
    print('#{}' .format(tc), (sum(M[:m])+d)%7)

#3
M = [3, 3, 1, 3, 2, 3, 2, 3, 3, 2, 3, 2]
for tc in range(int(input())):
    m, d = map(int, input().split())
    print(f'#{tc+1}', (sum(M[:m])+d)%7)