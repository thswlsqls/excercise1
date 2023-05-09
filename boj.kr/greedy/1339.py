N = int(input())
words = []
for _ in range(N):
    words.append(list(map(lambda c: ord(c)-65, input())))

alphabets = [0] * 26
for word in words:
    for i, c in enumerate(word[::-1]):
        alphabets[c] += 10 ** i
alphabets.sort(reverse=True)

n = 9
tot = 0
for i in range(9):
    tot += n*alphabets[i]
    n -= 1

print(tot)