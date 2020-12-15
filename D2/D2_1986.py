# 1986. 지그재그 숫자
# 1
n=[0]
for i in range(1,6):
    n.append(i)
    n.append(-i)
for tc in range(int(input())):
    print('#{} {}' .format(tc+1,n[int(input())]))

# 2
for tc in range(int(input())):
    N=int(input())+1
    print('#{} {}' .format(tc+1,N//2 if N%2==0 else -(N//2)))