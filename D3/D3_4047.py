def check():
    dic = {'S': [], 'D': [], 'H': [], 'C': []}
    a = input()
    for i in range(0, len(a), 3):
        if int(a[i+1]+a[i+2]) not in dic[a[i]]:
            dic[a[i]].append(int(a[i+1]+a[i+2]))
        else:
            print('ERROR')
            return
    for j in dic.values():
        print(13-len(j), end=' ')
    print()
 
 
for idx in range(1, int(input())+1):
    print('#{}' .format(idx), end=' ')
    check()