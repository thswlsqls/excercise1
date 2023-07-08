N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split()))
qs = '+' * ops[0] + '-' * ops[1] + '*' * ops[2] + '/' * ops[3]

def divide(a, b):
    if a < 0 and b > 0:
        return -1 * (abs(a) // b)
    return a // b
from itertools import permutations
max_ans = -int(1e9)
min_ans = int(1e9)
for permu in permutations(qs, N - 1):
    ans = nums[0]
    for i in range(N - 1):
        if permu[i] == '+':
            ans += nums[i + 1]
        elif permu[i] == '-':
            ans -= nums[i + 1]
        elif permu[i] == '*':
            ans *= nums[i + 1]
        elif permu[i] == '/':
            ans = divide(ans, nums[i + 1])
    max_ans = max(max_ans, ans)
    min_ans = min(min_ans, ans)

print(max_ans)
print(min_ans)