for tc in range(int(input())):
    t = 0
    for _ in range(int(input())):
        a, b = map(float, input().split())
        t += a*b
    print(f'#{tc+1} {t}')