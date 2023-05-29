T = int(input())
N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_sums = []
for i in range(len(N_list)):
    for j in range(i+1, len(N_list)+1):
        N_sub = N_list[i:j]
        N_sums.append(sum(N_sub))

M_sums = []
for k in range(len(M_list)):
    for l in range(k+1, len(M_list)+1):
        M_sub = M_list[k:l]
        M_sums.append(sum(M_sub))

N_sums.sort()
M_sums.sort()

from bisect import bisect_left, bisect_right

cnt = 0
for N_sum in N_sums:
    l = bisect_left(M_sums, T-N_sum)
    r = bisect_right(M_sums, T-N_sum)
    cnt += r-l

print(cnt)




