#1
for tc in range(int(input())):
    A,B=map(str,input().split())
    a=len(A)
    b=len(B)
    i=a-b
    j=c=0
    while j<=i:
        if A[j:j+b]==B:
            j+=b
        else:
            j+=1
        c+=1
    if a-j>0:
        c+=a-j
    print('#{} {}' .format(tc+1,c))

#2
for tc in range(int(input())):
    A,B=map(str,input().split())
    a=len(A)
    b=len(B)
    if B in A:
        a-=A.count(B)*(b-1)
    print('#{} {}' .format(tc+1,a))