N = int(input())
A = list(map(int, input().split()))

LIS = []
LIS.append(A[0])

from bisect import bisect_left

for a in A:
    if a > LIS[-1]:
        LIS.append(a)
    else:
        LIS[bisect_left(LIS, a)] = a

print(len(LIS))