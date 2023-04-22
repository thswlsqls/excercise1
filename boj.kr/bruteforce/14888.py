from itertools import permutations

N = int(input())
nums = list(map(int, input().split()))
ops_cnt = list(map(int, input().split()))
list = ['+', '-', '*', '//']
ops_list = []

for i in range(4):
    for _ in range(ops_cnt[i]):
        ops_list.append(list[i])

def divide(a, b):
    if a < 0 and b > 0:
        result = abs(a)//b
        result = -1 * result
        return result
    return a//b

max = -1e9
min = 1e9

for permu in permutations(ops_list, len(ops_list)):
    result = nums[0]
    for i in range(len(permu)):
        if permu[i] == '*':
            result *= nums[i+1]
        if permu[i] == '//':
            result = divide(result, nums[i+1])
        if permu[i] == '+':
            result += nums[i+1]
        if permu[i] == '-':
            result -= nums[i+1]
    min = result if result < min else min
    max = result if result > max else max

print(max)
print(min)