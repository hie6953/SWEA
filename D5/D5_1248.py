def f(s1):
    global s
    if s1:
        if vtd[s1]:
            s = s1
            return preord(s1)
        else:
            vtd[s1] = 1
            f(tree[s1][2])
 
 
def preord(s):
    global cnt
    if s:
        cnt += 1
        preord(tree[s][0])
        preord(tree[s][1])
 
 
for tc in range(1, int(input())+1):
    V, E, s1, s2 = map(int, input().split())
    lst = list(map(int, input().split()))
    #[0]자식1 [1]자식2 [2]부모
    tree = [[0]*3 for _ in range(V+1)]
    vtd = [0]*(V+1)
    for e in range(E):
        if tree[lst[e*2]][0] == 0:
            tree[lst[e*2]][0] = lst[e*2+1]
            tree[lst[e*2+1]][2] = lst[e*2]
        else:
            tree[lst[e*2]][1] = lst[e*2+1]
            tree[lst[e*2+1]][2] = lst[e*2]
    cnt = 0
    s = 0
    f(s1)
    f(s2)
    print('#{} {} {}' .format(tc, s, cnt))