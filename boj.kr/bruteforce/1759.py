from itertools import combinations

L, C = map(int, input().split())
clist = list(input().split())

vowels = ['a', 'e', 'i', 'o', 'u']

candidates = set()
for combi in combinations(clist, L):
    candidates.add(''.join(sorted(combi)))


passwords = []
for candidate in sorted(candidates):
    vowels_cnt = 0
    for v in vowels:
        if v in candidate:
            vowels_cnt += 1
    if 0<vowels_cnt<=L-2:
        passwords.append(candidate)

for password in sorted(passwords):
    print(password)
