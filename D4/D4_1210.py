def ladder():
    # 도착 지점 찾기
    for j in range(100):
        if lst[99][j] == 2:
            break
    for i in range(99, 0, -1):
        # 양사이드 범위 밖 안찾음
        # 좌우 1 있는지 찾아서 있으면 이동
        if j>0 and lst[i][j-1]:
            while j>0 and lst[i][j-1]:
                j -= 1
            
        elif j<99 and lst[i][j+1]:
            while j<99 and lst[i][j+1]:
                j += 1
    return j

def ladder1(lst):
    if i == 99:
        return j
    else:
        lst[99-i]

for idx in range(1, 2):
    input()
    lst = [list(map(int, input().split())) for _ in range(100)]
    print('#{} {}'.format(idx, ladder()))