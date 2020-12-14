# 최빈수 구하기
for _ in range(int(input())):
    N=input()
    student=list(map(int,input().split()))
    point=[0]*101
    mp=0
    for s in student:
        point[s]+=1
        if point[s]>point[mp]:
            mp=s
        elif point[s]==point[mp]:
            mp=max(s,mp)
    print('#{} {}' .format(N,mp))