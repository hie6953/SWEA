for tc in range(1, 11):
    input()
    lst = [list(map(int, input().split())) for _ in range(100)]
    ziplst = zip(*lst)
    m_lst = [0, 0]
    for i in range(100):
        m_lst.append(sum(lst[i]))
        m_lst[0] += lst[i][i]
        m_lst[1] += lst[99-i][i]
    for j in ziplst:
        m_lst.append(sum(j))
    print('#{} {}' .format(tc, max(m_lst)))