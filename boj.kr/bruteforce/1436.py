N = int(input())

name = 666
cnt = 1
while True:
    if str(name).__contains__("666"):
        if cnt == N:
            break
        cnt += 1
    name += 1

print(name)
