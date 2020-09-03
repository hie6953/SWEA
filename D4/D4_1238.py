def dfs(S):
    Q = [] # 큐 생성
    Q.append(S) # 시작 값 큐에 담기
    vtd[S] = 1 # 시작 값 방문 표시
    max_vtd = 1 # 방문의 최대값 초기화
    maxw = 1 # 방문 최대값 인덱스 초기화
    while Q: # 큐가 있을 때만 작동
        S = Q.pop(0) # 큐에 있는 첫번째 값 담기
        for w in G[S]: # S의 접점 w 
            if vtd[w] == 0: # w 방문 안했는지 확인
                Q.append(w) # 큐에 담기
                vtd[w] = vtd[S] + 1 # 얼마나 떨어져있는지 방문표시
                if vtd[w] == max_vtd and w > maxw: # 최대값과 같거나 크면
                    maxw = w # 최대값 인덱스 교체
                if vtd[w] > max_vtd: # 최대값보다 크면
                    max_vtd = vtd[w] # 최대값 교체
                    maxw = w # 최대값 인덱스 교체
    return maxw # 최대값 인덱스 리턴


for T in range(1, 11):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    vtd = [0]*101 # 1부터 100까지 방문만들어야해서 0번 안쓰고 101개만듬
    G = [[] for _ in range(101)] # 위와 같은이유로 101개 빈 리스트 만듬
    for n in range(N//2): # N개를 from과 to로 나누기 위해 2로 나눔
        G[lst[n*2]].append(lst[n*2+1]) # G의 인덱스에서 갈 수 있는 경로들을 담음
    print('#{} {}' .format(T, dfs(S))) # 테스트 케이스와 최대값 인덱스 출력