for tc in range(int(input())):
    sound = input()
    check = [0]*5
    max_cnt = cnt = 0
    for s in sound:
        if s == 'c':
            check[0]+=1
            cnt+=1
        elif s=='r':
            if check[0] > check[1]:
                check[1]+=1
            else:
                max_cnt=-1
                break
        elif s=='o':
            if check[1] > check[2]:
                check[2]+=1
            else:
                max_cnt=-1
                break
        elif s=='a':
            if check[2] > check[3]:
                check[3]+=1
            else:
                max_cnt=-1
                break
        elif s=='k':
            if check[3] > check[4]:
                check[4]+=1
                if cnt > max_cnt:
                    max_cnt = cnt
                cnt -= 1
            else:
                max_cnt=-1
                break
    if check[0] != check[4]:
        max_cnt = -1
    print('#{} {}' .format(tc+1, max_cnt))