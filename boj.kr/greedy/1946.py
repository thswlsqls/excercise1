import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    ranks = [list(map(int, input().split())) for _ in range(N)]
    ranks = sorted(ranks, key = lambda x : x[0])
    cur = ranks[0][1]
    cnt = 1
    for i in range(1, N):
        if ranks[i][1] < cur:
            cur = ranks[i][1]
            cnt += 1
    print(cnt)