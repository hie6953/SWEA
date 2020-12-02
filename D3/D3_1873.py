for tc in range(int(input())):
    H, W = map(int, input().split())
    HW = [list(map(str, input())) for _ in range(H)]

    N = int(input())
    Order = input()
    D = ['<','>','^','v']
    SD = [(0,-1),(0,1),(-1,0),(1,0)] # 슛방향
    for x in range(H):
        for y in range(W):
            now = HW[x][y]
            for d in D:
                if now == d:
                    h,w=x,y
                    break
    for o in Order:
        if o == 'U':
            if 0<=h-1 and HW[h-1][w] == '.':
                HW[h][w]='.'
                h-=1
            HW[h][w]='^'

        elif o == 'D':
            if h+1<H and HW[h+1][w] == '.':
                HW[h][w]='.'
                h+=1
            HW[h][w]='v'

        elif o == 'L':
            if 0<=w-1 and HW[h][w-1] == '.':
                HW[h][w]='.'
                w-=1
            HW[h][w]='<'

        elif o == 'R':
            if w+1<W and HW[h][w+1] == '.':
                HW[h][w]='.'
                w+=1
            HW[h][w]='>'

        elif o == 'S':
            n = HW[h][w]
            for i in range(4):
                if n == D[i]:
                    dh, dw = SD[i]
                    nh, nw = h+dh, w+dw
                    while 0<=nh<H and 0<=nw<W and HW[nh][nw]!='#':
                        if HW[nh][nw] == '*':
                            HW[nh][nw] = '.'
                            break
                        nh+=dh
                        nw+=dw
    print('#{}' .format(tc+1), end=' ')
    for hw in HW:
        print(*hw, sep='')