#1
for tc in range(int(input())):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if lst[i][0] < lst[j][0] and lst[i][1] > lst[j][1]:
                cnt += 1
            if lst[i][0] > lst[j][0] and lst[i][1] < lst[j][1]:
                cnt += 1
    print(f'#{tc+1} {cnt}')

#2
for tc in range(int(input())):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    lst.sort()
    cnt = 0
    for i in range(N-1):
        for j in range(i+1, N):
            if lst[i][0] < lst[j][0] and lst[i][1] > lst[j][1]:
                cnt += 1
    print(f'#{tc+1} {cnt}')