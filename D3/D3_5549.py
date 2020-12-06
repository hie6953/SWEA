for tc in range(int(input())):
    N=input()
    if int(N[-1])%2:
        r='Odd'
    else:
        r='Even'
    print('#{} {}' .format(tc+1,r))