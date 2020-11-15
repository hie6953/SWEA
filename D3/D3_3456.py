# 직사각형 길이 찾기
# 1
for tc in range(int(input())):
    a, b, c = map(int, input().split())
    if a==b:
        r=c
    elif a==c:
        r=b
    else:
        r=a
    print('#{} {}' .format(tc+1, r))

# 2
for tc in range(int(input())):
    e=input().split()
    for i in e:
        if e.count(i)%2:
            print(f"#{tc+1} {i}")
            break
