for tc in range(1, int(input())+1):
    N, M = map(int, input().split())
    A = [0]+list(map(int, input().split()))
    B = [0]+list(map(int, input().split()))
    V = [0]*(N+1)
    for i in range(1, M+1):
        for j in range(1, N+1):
            if A[j] <= B[i]:
                V[j] += 1
                break
    max_k = 1
    for k in range(1, N+1):
        if V[k] > V[max_k]:
            max_k = k
    print('#{} {}' .format(tc, max_k))