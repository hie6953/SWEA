for tc in range(int(input())):
    p, q = map(float, input().split())
    # s1은 처음에 방향안맞음 > 뒤집어서 제대로 꽂음
    # s1 = (1-p)*q
    # s2는 처음에 방향맞는데 잘못꽂음 > 뒤집어서 방향안맞음
    #  > 다시 방향맞추고 제대로 꽂음
    # s2 = p*(1-q)*q
    r='YES' if p*(1-q)*q > (1-p)*q else 'NO'
    print('#{} {}' .format(tc+1, r))


for t in range(int(input())):
    p,q=map(float,input().split())
    print(f'#{t+1} {"YES" if p*(1-q)*q>(1-p)*q else "NO"}')