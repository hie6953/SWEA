# D5 상원이의 생일파티 
#1
for tc in range(int(input())):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(M)]
    friends = [[] for _ in range(N+1)]
    invite = [0]*(N+1)
    invite[1] = 1
    for a, b in lst:
        friends[a].append(b)
        friends[b].append(a)
        if a == 1:
            invite[b] = 1
        if b == 1:
            invite[a] = 1
    cnt = len(friends[1])
    for i in friends[1]:
        for j in friends[i]:
            if invite[j] == 0:
                invite[j] = 1
                cnt += 1
    print('#{} {}' .format(tc+1, cnt))

#2
for tc in range(int(input())):
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(M)]
    friends = [[] for _ in range(N+1)]
    invite = [0]*(N+1)
    for a, b in lst:
        friends[a]+=[b]
        friends[b]+=[a]
    cnt = 0
    for i in friends[1]:
        if invite[i]==0:
            cnt+=1
        invite[i]=1
        for j in friends[i]:
            if j!=1 and invite[j] == 0:
                invite[j] = 1
                cnt += 1
    print('#{} {}' .format(tc+1, cnt))