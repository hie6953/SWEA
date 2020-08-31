def calculate(num_a, num_b, sign):
    if sign == '+':
        return str(int(num_a)+int(num_b))
    if sign == '*': 
        return str(int(num_a)*int(num_b))


icp = {'(':3, '*':2, '+':1, ')':0} # in-stack priority 스택 속 우선순위
isp = {'(':0, '*':2, '+':1} # in-coming priority 새로 읽은 연산자 우선순위
for idx in range(1, 2):
    input()
    lst = []
    stack = []
    for ch in input():
        if ch not in icp:
            lst.append(ch)
        else:
            if len(stack) == 0:
                stack.append(ch)
            elif ch == ")":
                while stack[-1] != "(":
                    lst.append(calculate(lst.pop(), lst.pop(), stack.pop()))
                stack.pop()
            else:
                if icp[ch] > isp[stack[-1]]:
                    stack.append(ch)
                else:
                    while len(stack) and icp[ch] <= isp[stack[-1]]:
                        lst.append(calculate(lst.pop(), lst.pop(), stack.pop()))
                    stack.append(ch)
    else:
        while len(stack):
            lst.append(calculate(lst.pop(), lst.pop(), stack.pop()))
    print('#{} {}' .format(idx, lst[0]))