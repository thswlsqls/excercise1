# 예제문제(3)
# boj/kr 1449 수리공 항승

N, L = map(int, input().split())
crood = [False for _ in range(1001)]
for i in map(int, input().split()):
    crood[i] = True

ans = 0
x = 0
while x < 1001:
    if crood[x]:
        x += L
        ans += 1
    else:
        x += 1

print(ans)