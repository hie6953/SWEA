for tc in range(1, int(input())+1):
    num = list(map(int, input().split()))
    total = set()
    for i in range(3):
        cnt=0
        cnt+=num[i]
        for j in range(i+1, 6):
            cnt+=num[j]
            for k in range(j+1, 7):
                cnt+=num[k]
                total.add(cnt)
                cnt-=num[k]
            cnt-=num[j]
    total = sorted(total)
    print('#{}' .format(tc), total[-5])