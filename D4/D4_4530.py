# 4530. 극한의 청소 작업
for tc in range(int(input())):
    A,B=input().split()
    sA,sB='1','1'
    if A[0]=='-':
        sA,A='-1',A[1:]
    if B[0]=='-':
        sB,B='-1',B[1:]    
    T=-1 if sA!=sB else 0
    lA,lB=len(A),len(B)
    for i in range(1,13):
        ai,bi=0,0
        if i <=lA:
            ai=int(A[-i])
        if i <=lB:
            bi=int(B[-i])
        ai = ai-1 if ai>4 else ai
        bi = bi-1 if bi>4 else bi
        T+=(int(sB)*bi-int(sA)*ai)*(9**(i-1))
    print('#{} {}' .format(tc+1,T))