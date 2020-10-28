import sys
sys.stdin = open('input.txt', 'r')

num = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111', '0111011', '0110111', '0001011']
for tc in range(int(input())):
    N, M = map(int, input().split())
    code = [input() for _ in range(N)]
    clst = []
    check = []
    total = 0
    for i in range(0, N, 10):
        if code[i] not in clst and code[i] != '0'*M:
            clst.append(code[i])
            nc = '0'*100+bin(int(code[i], 16))[2:]
            m = len(nc)-1
            while m > 56:
                if nc[m] != '0':
                    ratio = 1
                    while True:
                        # 마지막줄만 확인
                        rc1 = nc[m + 1 - 7 * ratio:m + 1]
                        rc2 = nc[m+1-14*ratio:m+1-7*ratio]
                        nrc1 = ''
                        nrc2 = ''
                        for j in range(0, 7*ratio, ratio):
                            nrc1 += rc1[j]
                        for j in range(0, 7*ratio, ratio):
                            nrc2 += rc2[j]
                        if nrc1 in num and nrc2 in num:
                            # 비밀번호 확인
                            pwd = ''
                            for k in range(0, 56*ratio, ratio):
                                pwd += nc[m + 1 - 56 * ratio:m + 1][k]
                            lst = []
                            for l in range(8):
                                for o in range(10):
                                    if num[o] == pwd[l*7:(l+1)*7]:
                                        lst.append(o)
                            if lst not in check:
                                check.append(lst)
                                t = 0
                                for p in range(8):
                                    if p % 2:
                                        t += lst[p]
                                    else:
                                        t += lst[p] * 3
                                total += sum(lst) if t % 10 == 0 else 0
                            m -= 56*ratio
                            break
                        ratio += 1
                else:
                    m -= 1
    print('#{} {}' .format(tc+1, total))