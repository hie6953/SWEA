#1
num = []
# 32대신 int(1000**1/2)+1 써도됨
for i in range(1, 32):
    if str(i) == str(i)[-1::-1] and str(i**2) == str(i**2)[-1::-1]:
        num.append(i**2)
for tc in range(int(input())):
    A, B = map(int, input().split())
    t = 0
    for n in num:
        if n<A:continue
        elif n>B:break
        else:t+=1
    print(f'#{tc+1} {t}')

#2
num = []
for i in range(1, 32):
    if str(i) == str(i)[-1::-1] and str(i**2) == str(i**2)[-1::-1]:
        num.append(i**2)
for tc in range(int(input())):
    A, B = map(int, input().split())
    t = 0
    for n in num:
        if A<=n<=B:
            t+=1
    print(f'#{tc+1} {t}')