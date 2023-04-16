# 18. Capter 2. 완전 탐색 - 예제문제 (3) -1
# boj.kr/2309 일곱 난쟁이

from itertools import combinations

arr = [int(input()) for _ in range(9)]
for combi in combinations(arr, 7):
    if sum(combi) == 100:
        for h in sorted(combi):
            print(h)
        break

arr = [int(input()) for _ in range(9)]
tot = sum(arr)
arr.sort()

def f():
    for i in range(8):
        for j in range(i+1, 9):
            if tot - (arr[i]+arr[j]) == 100:
                for k in range(9):
                    if k != i and k != j:
                        print(arr[k])
                return


f()