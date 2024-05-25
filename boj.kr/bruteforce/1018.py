N, M = map(int, input().split())
board = [input() for _ in range(N)]
cntBoard = [[0 for _ in range(M)] for _ in range(N)]
cntBoard2 = [[0 for _ in range(M)] for _ in range(N)]

# 짝수 row 짝수 col = 첫번째칸
# 짝수 row 홀수 col = 두번째칸
# 홀수 row 짝수 col = 두번째칸
# 홀수 row 홀수 col = 첫번째칸

for i in range(N):
    for j in range(M):
        if i % 2 == 0:
            if j % 2 == 0:
                if board[i][j] == 'B':
                    cntBoard[i][j] = 1
            if j % 2 == 1:
                if board[i][j] == 'W':
                    cntBoard[i][j] = 1
        if i % 2 == 1:
            if j % 2 == 0:
                if board[i][j] == 'W':
                    cntBoard[i][j] = 1
            if j % 2 == 1:
                if board[i][j] == 'B':
                    cntBoard[i][j] = 1

for i in range(N):
    for j in range(M):
        if i % 2 == 0:
            if j % 2 == 0:
                if board[i][j] == 'W':
                    cntBoard2[i][j] = 1
            if j % 2 == 1:
                if board[i][j] == 'B':
                    cntBoard2[i][j] = 1
        if i % 2 == 1:
            if j % 2 == 0:
                if board[i][j] == 'B':
                    cntBoard2[i][j] = 1
            if j % 2 == 1:
                if board[i][j] == 'W':
                    cntBoard2[i][j] = 1

cntList = []
cnt = 0

for i in range(N-7):
    for j in range(M-7):
        for k in range(8):
            for l in range(8):
                cnt += cntBoard[i+k][j+l]
        cntList.append(cnt)
        cnt = 0

for i in range(N-7):
    for j in range(M-7):
        for k in range(8):
            for l in range(8):
                cnt += cntBoard2[i+k][j+l]
        cntList.append(cnt)
        cnt = 0

print(sorted(cntList)[0])