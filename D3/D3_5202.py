for tc in range(int(input())):
    N = int(input())
    car = sorted([list(map(int, input().split())) for _ in range(N)])
    c = 0
    i = 1
    while i < len(car):
        if car[i-1][1] <= car[i][0]:
            i += 1
        elif car[i-1][1] >= car[i][1]:
            car.remove(car[i-1])
        elif car[i-1][1] < car[i][1]:
            car.remove(car[i])
    print('#{} {}' .format(tc+1, len(car)))