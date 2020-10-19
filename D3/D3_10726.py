for tc in range(int(input())):
    N, M = map(int, input().split())
    if (M-(2**N)+1)%(2**N):
        x='OFF'
    else:
        x='ON'
    print(f'#{tc+1} {x}') 