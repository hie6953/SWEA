for tc in range(int(input())):
    S = input()[-1::-1]
    n = ''
    for s in S:
        if s=='b':
           n+='d'
        elif s=='d':
            n+='b'
        elif s=='p':
            n+='q'
        elif s=='q':
            n+='p'
    print(f'#{tc+1} {n}')