for tc in range(int(input())):
    N, A, B = map(int, input().split())
    print(f'{tc+1} {min(A,B)} {max(A+B,N)-N}')