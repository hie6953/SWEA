# 1989. 초심자의 회문 검사
#1
for t in range(int(input())):
    text=input()
    l=len(text)//2
    r=0
    for i in range(l):
        if text[i]==text[-i-1]:r=1
        else:
            r=0
            break
    print('#{} {}' .format(t+1,r))

#2 
for tc in range(int(input())):
    text=input()
    nt=''
    for t in text:nt=t+nt
    print('#{} {}' .format(tc+1,1 if text==nt else 0))