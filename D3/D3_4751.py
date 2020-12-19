# 4751. 다솔이의 다이아몬드 장식
for tc in range(int(input())):
    P=['.','.','#','.','.']
    S=input()
    ls=len(S)
    for i in range(5):
        if i==0 or i==4:
            P[i]+='.#..'*ls
        elif i==1 or i==3:
            P[i]+='#.#.'*ls
        else:
            for s in S:
                P[i]+='.'+s+'.#'
    for p in P:
        print(p)
