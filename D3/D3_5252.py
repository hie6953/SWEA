# 5252. [파이썬 S/W 문제해결 최적화] 1일차 - 공통 단어 검색
for tc in range(int(input())):
    N,M=map(int,input().split())
    A = [[] for _ in range(26)]
    c=0
    for _ in range(N):
        a=input()
        A[ord(a[0])-97].append(a)
    for _ in range(M):
        b=input()
        bn=ord(b[0])-97
        for i in range(len(A[bn])):
            if A[bn][i]==b:
                A[bn].pop(i)
                c+=1
                break
    print('#{} {}' .format(tc+1,c))
     