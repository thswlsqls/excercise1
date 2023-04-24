# 1. 문자 리스트에서 L개 만큼 문자를 추출해 알파벳 순서로 정렬한 문자열을 candidates에 저장
# 2. candidates를 순회하면서 모음을 1개 이상, 자음을 2개 이상 포함하는지 검사해 passwords에 저장
# 3. passwords를 순회하면서 알파벳 순서대로 출력

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
