# def d(n) 정의, n의 각 자리수가 등차수열을 이루면 True 아니면 False
# 1부터 N까지 f(n)이 True인 개수를 출력

import math

N = int(input())
def f1(n, pc):
    return (n%math.pow(10, pc) - n%math.pow(10, pc-1))//math.pow(10, pc-1)

def f2(n):
    pc = 2
    list = []
    list.append(n%10)
    while n // math.pow(10, pc) > 0:
        list.append(f1(n, pc))
        pc += 1
    list.append(f1(n, pc))
    list.reverse()
    return list

def f3(list):
    diff = list[1] - list[0]
    for _ in range(1, len(list)):
        if list[_] - list[_-1] != diff:
            return False
    return True

def d(n):
    cnt = 0
    for _ in range(1, n+1):
        if f3(f2(_)):
            cnt += 1
    return cnt

print(d(N))