# # boj.kr/10815 숫자 카드

from bisect import bisect_left, bisect_right

N = int(input())
cards = sorted(map(int, input().split()))
M = int(input())
qry = list(map(int, input().split()))
ans = []

for q in qry:
    l = bisect_left(cards, q)
    r = bisect_right(cards, q)
    ans.append(1 if r-l else 0)

print(' '.join(map(str, ans)))
#print(*ans)