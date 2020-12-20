ans=[]
for tc in range(int(input())):
    A,B,C,D=map(int,input().split())
    a,b=A/B,C/D
    if a>b:r='ALICE'
    elif a<b:r='BOB'
    else:r='DRAW'
    ans.append((f'#{tc+1} {r}'))
for a in ans:
    print(a)