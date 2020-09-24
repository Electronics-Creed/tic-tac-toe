import cv2 as cv

game = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]
board = cv.imread('board.jpg')


def click_event(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDOWN:
        i = (x//210)*210
        j = (y//210)*210
        cv.line(board, (i + 20, j + 20), (i + 190, j + 190), (0, 0, 0), 4)
        cv.line(board, (i + 190, j + 20), (i + 20, j + 190), (0, 0, 0), 4)
        game[y//210][x//210] = 'X'
    elif event == cv.EVENT_RBUTTONDOWN:
        computer_turn()
    if declareWinner(game) == 1:
        print('You have won the game')
    if declareWinner(game) == -1:
        print('Computer has won the game')
    if board_is_full():
        if declareWinner(game) == 0:
            print('Tie')
    cv.imshow('board', board)


def computer_turn():
    global a, b
    bestscore = 10
    for i in range(0, 3):
        for j in range(0, 3):
            occupied = check(i, j)
            if not occupied:
                game[i][j] = 'O'
                score = minimax(game, True)
                game[i][j] = ' '
                if score < bestscore:
                    a = i
                    b = j
                bestscore = min(score, bestscore)
    game[a][b] = 'O'
    cv.circle(board, ((b * 210) + 105, (a * 210) + 105), 90, (0, 0, 0), 4)


def check(i, j):
    if game[i][j] == 'X' or game[i][j] == 'O':
        return True
    elif game[i][j] == ' ':
        return False


def minimax(game, maximizingPlayer):
    board = board_is_full()
    w = declareWinner(game)
    if board:
        return w
    if not board and (w == 1 or w == -1):
        return w
    if maximizingPlayer:
        maxeval = -10
        for i in range(0, 3):
            for j in range(0, 3):
                occupied = check(i, j)
                if not occupied:
                    game[i][j] = 'X'
                    eval = minimax(game, False)
                    game[i][j] = ' '
                    maxeval = max(eval, maxeval)
        return maxeval
    else:
        mineval = 10
        for m in range(0, 3):
            for n in range(0, 3):
                occupied = check(m, n)
                if not occupied:
                    game[m][n] = 'O'
                    eval = minimax(game, True)
                    game[m][n] = ' '
                    mineval = min(eval, mineval)
        return mineval


def declareWinner(game):
    u = 0
    while u < 3:
        if game[u][0] == game[u][1] == game[u][2] == 'X':
            return 1
        elif game[u][0] == game[u][1] == game[u][2] == 'O':
            return -1
        if game[0][u] == game[1][u] == game[2][u] == 'X':
            return 1
        elif game[0][u] == game[1][u] == game[2][u] == 'O':
            return -1
        u += 1
    if game[0][0] == game[1][1] == game[2][2] == 'X':
        return 1
    elif game[0][0] == game[1][1] == game[2][2] == 'O':
        return -1
    if game[0][2] == game[1][1] == game[2][0] == 'X':
        return 1
    elif game[0][2] == game[1][1] == game[2][0] == 'O':
        return -1
    return 0


def board_is_full():
    for i in range(0, 3):
        for j in range(0, 3):
            occupied = check(i, j)
            if not occupied:
                return False
    return True


cv.imshow('board', board)
cv.setMouseCallback('board', click_event)
cv.waitKey(0)
cv.destroyAllWindows()
