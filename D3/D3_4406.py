#1
for tc in range(1, int(input())+1):
    S = input()
    ans = ''
    m = ['a', 'e', 'i', 'o', 'u']
    for s in S:
        if s not in m:
            ans += s
    print('#{}' .format(tc), ans)

#2
for tc in range(1, int(input())+1):
    S = input()
    m = ['a', 'e', 'i', 'o', 'u']
    for s in S:
        if s in m:
            S=S.replace(s, '')
    print('#{}' .format(tc), S)