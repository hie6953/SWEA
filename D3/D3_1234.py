# 1234. [S/W 문제해결 기본] 10일차 - 비밀번호
for i in range(1,11):
    N,nums=input().split()
    P=''
    for n in range(int(N)):
        if P:
            if P[-1]==nums[n]:
                P=P[:-1]
            else:
                P+=nums[n]
        else:
            P+=nums[n]
    print('#{} {}' .format(i,P))
