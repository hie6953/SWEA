for tc in range(1, int(input())+1):
    D, A, B, F = map(int, input().split())
    print('#{} {}' .format(tc, D/(A+B)*F))