for tc in range(1, int(input())+1):
    N = int(input())
    farm = [list(map(int, input()))+[0] for _ in range(N)]
    ans = 0
    j = 0
    for i in range(N):
        crop = farm[i][N//2-j:N//2+j+1] 
        ans += sum(crop)
        if i < N//2:
            j += 1
        else:
            j -= 1
    print('#{}' .format(tc), ans)