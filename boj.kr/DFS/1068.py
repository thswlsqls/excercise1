import sys
sys.setrecursionlimit(10**6)

N = int(input())
parents = list(map(int, input().split()))
delete = int(input())

def dfs(node):
    parents[node] = -2
    for i in range(N):
        if parents[i] == node:
            dfs(i)

dfs(delete)

leaf_cnt = 0
for i in range(N):
    if parents[i] != -2 and i not in parents:
        leaf_cnt += 1

print(leaf_cnt)