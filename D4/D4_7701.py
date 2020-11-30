# 7701 염라대왕의 이름 정렬
for tc in range(int(input())):
    books_list =[[] for _ in range(51)]
    N = int(input())
    for _ in range(N):
        name = list(map(ord, input()))
        books_list[len(name)].append(name)
    print(f'#{tc+1}')
    for books in books_list[1:]:
        if books:
            books.sort()
            result = ['']
            for book in books:
                n = ''
                for b in book:
                    n += chr(b)
                if result[-1] != n:
                    result.append(n)
            for r in result[1:]:
                print(r)