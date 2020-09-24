import cv2.cv2 as cv


def coordinates(x, y):
    if 0 < x < 210 and 0 < y < 210:
        return 0, 0
    elif 210 < x < 420 and 0 < y < 210:
        return 0, 1
    elif 420 < x < 630 and 0 < y < 210:
        return 0, 2
    elif 210 < y < 420 and 0 < x < 210:
        return 1, 0
    elif 210 < y < 420 and 210 < x < 420:
        return 1, 1
    elif 210 < y < 420 and 420 < x < 630:
        return 1, 2
    elif 420 < y < 630 and 0 < x < 210:
        return 2, 0
    elif 420 < y < 630 and 210 < x < 420:
        return 2, 1
    elif 420 < x < 630 and 420 < y < 630:
        return 2, 2


def click_event(event, x, y, flags, para):
    if event == cv.EVENT_LBUTTONDOWN:
        j, i = coordinates(x, y)
        game[i][j] = 'X'

        i = (i * 210)
        j = (j * 210)

        cv.line(board, (i + 20, j + 20), (i + 190, j + 190), (0, 0, 0), 4)
        cv.line(board, (i + 190, j + 20), (i + 20, j + 190), (0, 0, 0), 4)
        cv.destroyAllWindows()


def user_turn():
    cv.setMouseCallback('board', click_event)


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
    cv.circle(board, ((a * 210) + 105, (b * 210) + 105), 105, (0, 0, 0), 4)


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


def print_winner(game):
    declare = declareWinner(game)
    if declare == 1 or declare == -1:
        cv.imshow('board', board)
        cv.waitKey(3000)
        cv.destroyAllWindows()

    if declare == 1:
        print('You have won the game')

        exit(0)
    elif declare == -1:
        print('Computer has won the game')
        exit(0)

    if board_is_full():
        if declareWinner(game) == 0:
            print('Tie')
        exit(0)


game = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]
board = cv.imread('board.jpg')
z = 0

while True:
    if z % 2 == 0:
        cv.imshow('board', board)
        user_turn()
    else:
        computer_turn()
    print_winner(game)
    cv.imshow('board', board)

    if z % 2 == 0:
        cv.waitKey(0)

    z += 1
