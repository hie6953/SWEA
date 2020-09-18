for tc in range(1, int(input())+1):
    P, Q, R, S, W = map(int, input().split())
    A, B = P*W, Q
    if W > R:
        B += (W-R)*S
    print('#{} {}' .format(tc, min(A, B)))