# 항구에 들어오는 배
for tc in range(int(input())):
    N = int(input())
    day = [int(input()) for _ in range(N)]
    ship = [day[1]-1]
    for i in range(2, N):
        d = day[i]-1
        c = len(ship)
        for s in ship:
            if d%s:
                c -= 1
            else:
                break
        if c == 0:
            ship.append(d)
    print('#{} {}' .format(tc+1, len(ship)))