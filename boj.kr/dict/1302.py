# 예제문제 (4)
# boj.kr/1302 베스트셀러
# 맵

books = dict()
for _ in range(int(input())):
    book = input()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

max = max(books.values())
candi = []
for k, v in books.items():
    if max == v:
        candi.append(k)

candi.sort()
print(candi[0])

print(f'candi: {candi}')