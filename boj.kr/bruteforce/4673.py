# def d(n) 정의
# 1부터 10000까지 수를 인자로 갖는 d(n)을 모두 저장
# 저장한 리스트를 정렬
# 정렬한 리스트에서 가장 작은 값부터 10000 이하 수를 출력

import math

def f(n, pc):
    return (n%math.pow(10, pc) - n%math.pow(10, pc-1))//math.pow(10, pc-1)
def d(n):
    result = n+n%10
    pc = 2
    while n // math.pow(10, pc) > 0:
        result += f(n, pc)
        pc += 1
    result += f(n, pc)
    return result

list = []
for _ in range(10000):
    list.append(d(_))

for _ in range(10000):
    if list.__contains__(_) == False:
        print(_)


