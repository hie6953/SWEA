# 1940. 가랏! RC카!
for t in range(int(input())):
    N=int(input())
    r=0
    last=0
    for _ in range(N):
        command=list(map(int,input().split()))
        if command[0]==0:
            pass
        elif command[0]==1:
            last+=command[1]
        else:
            last = max(last-command[1],0)
        r+=last
    print('#{} {}' .format(t+1,r))