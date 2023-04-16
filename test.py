# 예제문제 (1)
# boj.kr/9012 괄호
# 스택
#
# for _ in range(int(input())):
#     stk = []
#     isVPS = True
#     for ch in input():
#         if ch == '(':
#             stk.append(ch)
#         else:
#             if stk:
#                 stk.pop()
#             else:
#                 isVPS = False
#                 break
#
#     if stk:
#         isVPS = False
#
#     print("YES" if isVPS else "NO")

# 예제문제 (2)
# boj.kr/2164 카드2
# 큐
#
# from collections import deque
#
# dq = deque(range(1, int(input())+1))
#
# while len(dq) > 1:
#     dq.popleft()
#     dq.append(dq.popleft())
#
# print(dq.pop())

# 예제문제 (3)
# boj.kr/11286 절댓값 힙
# 우선순위 큐
#
# import sys
# import heapq as hq
#
# input = sys.stdin.readline
# arr = []
#
# for _ in range(int(input())):
#     n = int(input())
#     if n:
#         hq.heappush(arr, (abs(n), n))
#     else:
#         print(hq.heappop(arr)[1] if arr else 0)

# import sys
# import heapq as hq
#
# input = sys.stdin.readline
# min_heap = []
# max_heap = []
#
# for _ in range(int(input())):
#     n = int(input())
#     if n > 0:
#         hq.heappush(min_heap, n)
#     elif n < 0:
#         hq.heappush(max_heap, -n)
#     else:
#         if min_heap:
#             if max_heap:
#                 if min_heap[0] < abs(-max_heap[0]):
#                     print(hq.heappop(min_heap))
#                 else:
#                     print(-hq.heappop(max_heap))
#             else:
#                 print(hq.heappop(min_heap))
#         else:
#             if max_heap:
#                 print(-hq.heappop(max_heap))
#             else:
#                 print(0)

# 예제문제 (4)
# boj.kr/1302 베스트셀러
# 맵

# books = dict()
# for _ in range(int(input())):
#     book = input()
#     if book in books:
#         books[book] += 1
#     else:
#         books[book] = 1
#
# max = max(books.values())
# candi = []
# for k, v in books.items():
#     if max == v:
#         candi.append(k)
#
# candi.sort()
# print(candi[0])
#
# print(f'candi: {candi}')

# from itertools import permutations
# from itertools import combinations
#
# v = [1, 2, 3, 4]
# for i in permutations(v, 4):
#      print("p: ", i)
#
# for j in combinations(v, 2):
#     print("c: ", j)

# 18. Capter 2. 완전 탐색 - 예제문제 (3) -1
# boj.kr/2309 일곱 난쟁이
#
# from itertools import combinations
#
# arr = [int(input()) for _ in range(9)]
# for combi in combinations(arr, 7):
#     if sum(combi) == 100:
#         for h in sorted(combi):
#             print(h)
#         break
#
# arr = [int(input()) for _ in range(9)]
# tot = sum(arr)
# arr.sort()
#
# def f():
#     for i in range(8):
#         for j in range(i+1, 9):
#             if tot - (arr[i]+arr[j]) == 100:
#                 for k in range(9):
#                     if k != i and k != j:
#                         print(arr[k])
#                 return
#
#
# f()

# 탐욕법
# boj/kr 11047 동전 0
# 예제문제(2)
#
# N, K = map(int, input().split())
# coins = [int(input()) for _ in range(N)]
# coins.reverse()
# ans = 0
#
# for coin in coins:
#     ans += K // coin
#     K %= coin
#
# print(ans)

# 예제문제(3)
# boj/kr 1449 수리공 항승
#
# N, L = map(int, input().split())
# crood = [False for _ in range(1001)]
# for i in map(int, input().split()):
#     crood[i] = True
#
# ans = 0
# x = 0
# while x < 1001:
#     if crood[x]:
#         x += L
#         ans += 1
#     else:
#         x += 1
#
# print(ans)

# DFS
# adj = [[0]*13 for _ in range(13)]
#
# def dfs(now):
#     for nxt in range(13):
#         if adj[now][nxt]:
#             dfs(nxt)
#
# dfs(0)

# BFS
# from collections import deque
#
# adj = [[0]*13 for _ in range(13)]
#
# def bfs():
#     dq = deque()
#     dq.append(0)
#     while dq:
#         now = dq.popleft()
#         for nxt in range(13):
#             if adj[now][nxt]:
#                 dq.append(nxt)
#
# bfs()

# 길찾기 문제
# from collections import deque
#
# dy = (0, 1, 0, -1)
# dx = (1, 0, -1, 0)
# chk = [[False]*100 for _ in range(100)]
# N = int(input())
#
# def is_valid_coord(y, x):
#     return 0 <= y < N and 0 <= x < N
#
# def bfs(start_y, start_x):
#     q = deque()
#     q.append((start_y, start_x))
#     while len(q) > 0:
#         y, x = q.popleft()
#         chk[y][x] = True
#         for k in range(4):
#             ny = y + dy[k]
#             nx = x + dx[k]
#             if is_valid_coord(ny, nx) and not chk[ny][nx]:
#                 q.append((ny, nx))

# boj.kr/11724 연결 요소의 개수
# import sys
#
# sys.setrecursionlimit(10**6)
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# adj = [[0]*N for _ in range(N)]
# chk = [False]*N
# ans = 0
#
# for _ in range(M):
#     u, v = map(lambda x: x-1, map(int, input().split()))
#     adj[u][v] = adj[v][u] = 1
#
# def dfs(now):
#     for nxt in range(N):
#         if adj[now][nxt] and not chk[nxt]:
#             chk[nxt] = True
#             dfs(nxt)
#
# for i in range(N):
#     if not chk[i]:
#         ans += 1
#         chk[i] = True
#         dfs(i)
#
# print(ans)

# boj.kr/2178 미로 탐색
# from collections import deque
#
# dy = (0, 1, 0, -1)
# dx = (1, 0, -1, 0)
# N, M = map(int, input().split())
# board = [input() for _ in range(N)]
#
# def is_valid_coord(y, x):
#     return 0<=y<N and 0<=x<M
#
# def bfs(start_y, start_x):
#     chk = [[False] * M for _ in range(N)]
#     chk[start_y][start_x] = True
#     dq = deque()
#     dq.append((start_y, start_x, 1))
#
#     while dq:
#         y, x, d = dq.popleft()
#
#         if y == N-1 and x == M-1:
#             return d
#
#         nd = d + 1
#         for k in range(4):
#             ny = y + dy[k]
#             nx = x + dx[k]
#             if is_valid_coord(ny, nx) and not chk[ny][nx] and board[ny][nx] == '1':
#                 chk[ny][nx] = True
#                 dq.append((ny, nx, nd))
#
# print(bfs(0, 0))

# 이진 탐색 Binary Search
# 탐색 전에 반드시 정렬되어 있어야 한다.
# 살펴보는 범위를 절반 씩 줄여가면서 답을 찾는다.

# 정렬 O(NlogN) + 이진탐색 O(logN) => 결과적으로 O(NlogN)
# 미리 정렬되어 들어오면 이진탐색만 하면 되므로 O(logN)
# 일차원 배열에서 탐색행위가 1회일때는 선형탐색이 유리하지만(O(N) < O(NlogN), 여러번 하는 경우에는 이진탐색이 유리하다.(O(N^2) > O(NlogN))

# bisect_left/right
# from bisect import bisect_left, bisect_right
#
# v = (0, 1, 3, 3, 6, 6, 6, 7, 8, 8, 9)
# three = bisect_right(v, 3) - bisect_left(v, 3)
# four = bisect_right(v, 4) - bisect_left(v, 4)
# six = bisect_right(v, 6) - bisect_left(v, 6)
#
# print(f'number of 3: {three}') # 2
# print(f'number of 4: {four}') # 0
# print(f'number of 6: {six}') # 3

# 파라메트릭 서치
# 최적화 문제를 결정 문제로 바꿔서 이진탐색으로 푸는 방법이다.
# 최적화 문제 - 문제상황을 만족하는 변수의 최솟값, 최댓값을 구하는 문제
# 결정 문제 - YES/NO Problem
# 매개변수 Parameter가 주어지면 true or false가 결정되어야 한다.
# 가능한 해의 영역이 연속적이어야 한다.
# 범위를 반씩 줄여가면서 가운데 값이 true인지 false인지 구한다.
# 이진탐색과 똑같은 원리

# #boj.kr/2512 예산
# #
# N = int(input())
# req = list(map(int, input().split()))
# M = int(input())
#
# lo = 0
# hi = max(req)
# mid = (lo + hi) // 2
# ans = 0
#
# def is_possible(mid):
#     return sum(min(r, mid) for r in req) <= M
#
# while lo <= hi:
#     print(f'lo: {lo}, mid: {mid}, hi: {hi}, ans: {ans}')
#     if is_possible(mid):
#         lo = mid +1
#         ans = mid
#     else:
#         hi = mid -1
#
#     mid =(lo + hi) //2
#
# print(ans)

# # boj.kr/10815 숫자 카드
#
# from bisect import bisect_left, bisect_right
#
# N = int(input())
# cards = sorted(map(int, input().split()))
# M = int(input())
# qry = list(map(int, input().split()))
# ans = []
#
# for q in qry:
#     l = bisect_left(cards, q)
#     r = bisect_right(cards, q)
#     ans.append(1 if r-l else 0)
#
# print(' '.join(map(str, ans)))
# #print(*ans)

# Chapter 6.
# 동적 계획법

# 문제를 쪼개서 작은 문제의 답을 구하고, 그걸로 더 큰 문제의 답을 구하는 것을 반복함
# 분할 정복과 비슷한 느낌임

# DP 구현 2가지
# Top-down : 구현-재귀 저장방식-메모이제이션(Memoization)
# Bottom-up : 구현-반복문 저장방식-타뷸레이션(Tabulation)

# Memoization - 한 번 구한 답들은 저장해두자
# 부분 문제들의 답을 한 번 구했으면 또 구하지 않도록(중복연산 방지)
# Cache에 저장해두고 다음부턴 갖다 쓰자
# 필요한 부분 문제들만 구한다 Lazy-Evaluation
# Top-down 방식에서 사용함

# 4살 아이한테 메모이제이션을 설명하기
# 아빠 : 1+1+1+1+1..= 정답이 뭘까?
# 아이 : n이요
# 아빠 : 1을 붙여쓰고, 이번에는?
# 아이:  n+1이요.
# 아빠: 어떻게 그렇게 빨리 알았니?
# 아이: 하나 더했으니까요
# 아빠: n이라는 것을 기억하고 있으니 다시 계산할 필요가 없었구나

# 미리 다 구해두자 Tabulation
# 부분 문제들의 답을 미리 다 구해두면 편하다
# 테이블을 채워나간다는 의미라서 타불레이션
# 필요 없는 부분 문제들까지 전부 구한다 Eager-Evaluation
# Bottom-up 방식에서 사용

# 피보나치 수열
# f(0) = 0
# f(1) = 1
# f(i+2) = f(i+1) + f(i)

# boj.kr/2748
# 피보나치 수 2
# 메모이제이션 - 순서가 덜중요
# cache = [-1] * 91
# cache[0] = 0
# cache[1] = 1
# cnt = 0
#
# def f(n):
#     if cache[n] == -1:
#          cache[n] = f(n-1) + f(n-2)
#     return cache[n]
#
# print(f(int(input())))
#
#테뷸레이션 - 순서가 중요
# N = int(input())
# cache = [-1] * 91
# cache[0] = 0
# cache[1] = 1
#
# for i in range(2, N+1):
#     cache[i] = cache[i - 1] + cache[i - 2]
#
# print(cache[N])

# 이항계수 nCr
# bino(n,0) = 1
# bino(n,n) = 1
# bino(n,r) = bino(n-1, r-1) + bino(n-1, r)
# 삼각수로 확인가능, 맨위, 좌우를 1로 채우고 좌우 위에서 더한 값을 저장하는 것을 반복

# boj.kr/11051
# 이항계수 2
# 메모이제이션
# import sys
# sys.setrecursionlimit(10 ** 7)
#
# MOD = 10007
# cache = [[0] * 1001 for _ in range(1001)]
# N, K = map(int, input().split())
#
# def bino(n, k):
#     if cache[n][k]:
#         return cache[n][k]
#
#     if k == 0 or k == n:
#         cache[n][k] = 1
#     else:
#         cache[n][k] = bino(n-1, k-1) + bino(n-1, k)
#         cache[n][k] %= MOD
#
#     return cache[n][k]
#
# print(bino(N, K))

#타뷸레이션
#
# MOD = 10007
#
# cache = [[0] * 1001 for _ in range(1001)]
# N, K = map(int, input().split())
#
# for i in range(1001):
#     cache[i][0] = cache[i][i] = 1
#     for j in range(1, i):
#         cache[i][j] = cache[i-1][j-1] + cache[i-1][j]
#         cache[i][j] %= MOD
#
# print(cache[N][K])

# DP 구현 2가지
# Top-down
# 재귀, 메모이제이션, 직관적이라 코드 가독성이 좋다, 재귀함수 호출을 많이 해서 느릴 수 있다.
# Bottom-up
# 반복문, 타뷸레이션, 시간과 메모리를 좀 더 아낄 수도 있다. DP테이블을 채워나가는 순서를 알아야 한다.

# boj.kr/11726
# 2*n 타일링
#
# MOD = 10_007
#
# dp = [0]*1001
# dp[1] = 1
# dp[2] = 2
# n = int(input())
# for i in range(3, 1001):
#     dp[i] = (dp[i-1] + dp[i-2]) % MOD
#
# print(dp[n])

# boj.kr/10844
# 쉬운 계단 수
# MOD = 1_000_000_000
# #cache[n][d]: 길이가 n, 마지막 숫자가 d인 계단수 개수
# cache = [[0] * 10 for _ in range(101)]
# for j in range(1, 10):
#     cache[1][j] = 1
#
# for i in range(2, 101):
#     for j in range(10):
#         if j > 0:
#             cache[i][j] += cache[i-1][j-1]
#             cache[i][j] %= MOD
#         if j < 9:
#             cache[i][j] += cache[i-1][j+1]
#             cache[i][j] %= MOD
#
# ans = 0
# N = int(input())
# for j in range(10):
#     ans += cache[N][j]
#     ans %= MOD
#
# print(ans)

# 정리
# 동적계획법은 문제를 쪼개서 작은 문제부터 구해가며 원래 문제의 답을 구하는 방식
# 메모이제이션
# 점화식을 찾고 테이블만 잘 정의하면 풀리는 문제들이 많다. 점화식 찾기가 쉽지 않다.


# import sys
# input = sys.stdin.readline
#
# N = int(input())
# req = list(map(int, input().split()))
# M = int(input())
#
# lo = 0
# hi = max(req)
# mid = (lo+hi)//2
# ans = mid
#
# def is_possible(mid):
#     return sum(min(mid, r) for r in req) <= M
#
# while lo <= hi:
#     if is_possible(mid):
#         lo = mid + 1
#     else:
#         hi = mid - 1
#
#     mid = (lo + hi)//2
#     ans = mid
#
# print(ans)
#
# import sys
# input = sys.stdin.readline
# from bisect import bisect_left, bisect_right
#
# N = int(input())
# cardsA = list(map(int, input().split()))
# M = int(input())
# cardsB = list(map(int, input().split()))
# cardsA.sort()
# ans = []
#
# for c in cardsB:
#     l = bisect_left(cardsA, c) # 같거나 큰값중 첫번째
#     r = bisect_right(cardsA, c) # 큰값중 첫번째
#     ans.append(1 if r-l else 0)
#
# print(*ans)
#
# cache = [-1] * 91
# cache[0] = 0
# cache[1] = 1
#
# def fab(n):
#     if cache[n] == -1:
#         cache[n] = fab(n-1) + fab(n-2)
#     return cache[n]
#
# print(fab(int(input())))
#
# N = int(input())
# cache = [-1] * 91
# cache[0] = 0
# cache[1] = 1
#
# for i in range(2, N+1):
#     cache[i] = cache[i-1] + cache[i-2]
#
# print(cache[N])

# import sys
# sys.setrecursionlimit(10 ** 7)
#
# MOD = 10_007
# N, K = map(int, input().split())
# cache = [[0]*1001 for _ in range(1001)]
#
# def f(n, k):
#     if cache[n][k]:
#         return cache[n][k]
#
#     if k == 0 or n == k:
#         cache[n][k] = 1
#     else:
#         cache[n][k] = f(n-1, k-1) + f(n-1, k)
#         cache[n][k] %= MOD
#
#     return cache[n][k]
#
# print(f(N, K))

# MOD = 10_007
# cache = [[0]*1001 for _ in range(1001)]
# N, K = map(int, input().split())
#
# for i in range(1001):
#     cache[i][0] = cache[i][i] = 1
#     for j in range(1, i):
#         cache[i][j] = cache[i-1][j-1] + cache[i-1][j]
#         cache[i][j] %= MOD
#
# print(cache[N][K])

# import sys
# sys.setrecursionlimit(10 ** 7)
#
# MOD = 10_007
#
# cache = [0]*1001
# cache[1] = 1
# cache[2] = 2
#
# def f(n):
#     if cache[n] == 0:
#         cache[n] = f(n-1) + f(n-2)
#         cache[n] %= MOD
#
#     return cache[n]
#
# print(f(int(input())))

# MOD = 10_007
# cache = [0] * 1001
# cache[1] = 1
# cache[2] = 2
#
# N = int(input())
#
# for i in range(3, N+1):
#     cache[i] = cache[i-1] + cache[i-2]
#     cache[i] %= MOD
#
# print(cache[N])

# boj.kr / 10844
MOD = 1_000_000_000
# cache[n][d] = 길이가 n, 마지막 수가 d인 계단수 개수
cache = [[0]*10 for _ in range(101)]

for i in range(1, 10):
    cache[1][i] = 1

for j in range(2, 101):
    for k in range(10):
        if k > 0:
            cache[j][k] += cache[j-1][k-1]
            cache[j][k] %= MOD
        if k < 9:
            cache[j][k] += cache[j-1][k+1]
            cache[j][k] %= MOD

ans = 0
N = int(input())
for l in range(10):
    ans += cache[N][l]
    ans %= MOD

print(ans)


















































