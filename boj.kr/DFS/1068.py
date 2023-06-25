N = int(input())
tree = list(map(int, input().split()))
delete = int(input())
import sys
sys.setrecursionlimit(10**9)
def dfs(parent):
    tree[parent] = -2
    for i in range(N):
        if tree[i] == parent:
            dfs(i)
dfs(delete)
cnt = 0
for j in range(N):
    if tree[j] != -2 and j not in tree:
        cnt += 1
print(cnt)