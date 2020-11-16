#1
for tc in range(int(input())):
    S = input()
    c=[0]*123
    for s in S:
        c[ord(s)]+=1
    print('#{}' .format(tc+1), end=' ')
    t=0
    for i in range(97,123):
        if c[i]%2==1:
            print(chr(i),end='')
        else:
            t+=1
    if t==26:
        print('Good')
    else:
        print()


#2
for tc in range(int(input())):
    S = input()
    # 아스키 97~122
    c=[0]*123
    for s in S:
        c[ord(s)]+=1
    r=''
    for i in range(97,123):
        if c[i]%2==1:
            r+=chr(i)
    if r=='':
        r='Good'
    print('#{} {}' .format(tc+1, r))