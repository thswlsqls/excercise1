# 예제문제 (1)
# boj.kr/9012 괄호
# 스택

for _ in range(int(input())):
    stk = []
    isVPS = True
    for ch in input():
        if ch == '(':
            stk.append(ch)
        else:
            if stk:
                stk.pop()
            else:
                isVPS = False
                break

    if stk:
        isVPS = False

    print("YES" if isVPS else "NO")