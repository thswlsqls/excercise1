L, C = map(int, input().split())
words = list(input().split())
vowels = []

for w in words:
    for w in ('a', 'e', 'i', 'o', 'u'):
        vowels.append(w)

passwords = []
from itertools import combinations
for combi in combinations(words, L):
    v_cnt = 0
    for c in combi:
        if c in vowels:
            v_cnt += 1
    if 0 < v_cnt <= L-2:
        passwords.append(''.join(sorted(list(combi))))

for password in sorted(passwords):
    print(password)

