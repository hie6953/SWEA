for tc in range(int(input())):
    N = int(input())
    D = list(input().split())
    DA, DB = D[:N//2], D[N//2+1:] if N%2 else D[N//2:]
    s = D[N//2] if N%2 else ''
    print(f'#{tc+1}', end=' ')
    for i in range(N//2):
        print(DA[i], DB[i], end=' ')
    print(s)