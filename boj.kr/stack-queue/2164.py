# 예제문제 (2)
# boj.kr/2164 카드2
# 큐

from collections import deque

dq = deque(range(1, int(input())+1))

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq.pop())
