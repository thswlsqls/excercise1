N, M = map(int, input().split())
board = [input() for _ in range(N)]

cntBoardB = [[0 for _ in range(M)] for _ in range(N)]
cntBoardW = [[0 for _ in range(M)] for _ in range(N)]

for r in range(N):
    for c in range(M):
        if r % 2 == 0:
            if c % 2 == 0:
                if board[r][c] == 'W':
                    cntBoardB[r][c] = 1
                if board[r][c] == 'B':
                    cntBoardW[r][c] = 1
            if c % 2 == 1:
                if board[r][c] == 'B':
                    cntBoardB[r][c] = 1
                if board[r][c] == 'W':
                    cntBoardW[r][c] = 1
        if r % 2 == 1:
            if c % 2 == 0:
                if board[r][c] == 'B':
                    cntBoardB[r][c] = 1
                if board[r][c] == 'W':
                    cntBoardW[r][c] = 1
            if c % 2 == 1:
                if board[r][c] == 'W':
                    cntBoardB[r][c] = 1
                if board[r][c] == 'B':
                    cntBoardW[r][c] = 1

cntList = []
cntB = 0
cntW = 0

for i in range(N-7):
    for j in range(M-7):
        for k in range(8):
            for l in range(8):
                cntB += cntBoardB[i+k][j+l]
                cntW += cntBoardW[i+k][j+l]
        cntList.append(cntB)
        cntList.append(cntW)
        cntB = 0
        cntW = 0

print(sorted(cntList)[0])