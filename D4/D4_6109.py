# 추억의 2048게임
for tc in range(int(input())):
    N,O=map(str,input().split())
    N=int(N)
    box=[list(map(int,input().split())) for _ in range(N)]
    if O=='up':
        for i in range(N):
            now=j=0
            while j<N:
                if box[j][i]==0:j+=1
                elif box[now][i]==0:
                    box[now][i]=box[j][i]
                    box[j][i]=0
                    j+=1
                elif now==j:j+=1
                else:
                    if box[now][i]==box[j][i]:
                        box[now][i]*=2
                        box[j][i]=0
                        now+=1
                        j+=1
                    elif box[now][i]!=box[j][i]:now+=1
    elif O=='down':
        for i in range(N):
            now=j=N-1
            while j>=0:
                if box[j][i]==0:j-=1
                elif box[now][i]==0:
                    box[now][i]=box[j][i]
                    box[j][i]=0
                    j-=1
                elif now==j:j-=1
                else:
                    if box[now][i]==box[j][i]:
                        box[now][i]*=2
                        box[j][i]=0
                        now-=1
                        j-=1
                    elif box[now][i]!=box[j][i]:now-=1
    elif O=='left':
        for i in range(N):
            now=j=0
            while j<N:
                if box[i][j]==0:j+=1
                elif box[i][now]==0:
                    box[i][now]=box[i][j]
                    box[i][j]=0
                    j+=1
                elif now==j:j+=1
                else:
                    if box[i][now]==box[i][j]:
                        box[i][now]*=2
                        box[i][j]=0
                        now+=1
                        j+=1
                    elif box[i][now]!=box[i][j]:now+=1
    elif O=='right':
        for i in range(N):
            now=j=N-1
            while j>=0:
                if box[i][j]==0:j-=1
                elif box[i][now]==0:
                    box[i][now]=box[i][j]
                    box[i][j]=0
                    j-=1
                elif now==j:j-=1
                else:
                    if box[i][now]==box[i][j]:
                        box[i][now]*=2
                        box[i][j]=0
                        now-=1
                        j-=1
                    elif box[i][now]!=box[i][j]:now-=1
    print(f'#{tc+1}')
    for b in box:
        print(*b)