N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]

from collections import deque
def bfs(n):
    dq = deque()
    dq.append(n)

    while dq:
        cur = dq.popleft()
        if cur == n and adj[n-1][n-1] == 1 :
            break
        adj[n-1][n-1] = 1
        for i in range(M):
            if board[i][0] == cur and not adj[n-1][board[i][1]-1] :
                adj[n-1][board[i][1]-1] = adj[n-1][board[i][0]-1] + 1
                dq.append(board[i][1])
            if board[i][1] == cur and not adj[n-1][board[i][0]-1] :
                adj[n-1][board[i][0]-1] = adj[n-1][board[i][1]-1] + 1
                dq.append(board[i][0])

tot_list = []
for i in range(1, N+1):
    adj = [[0] * N for _ in range(N)]
    bfs(i)
    tot_list.append([i, sum(adj[i-1])])

tot_list.sort(key = lambda x : (x[1], x[0]))
print(tot_list[0][0])