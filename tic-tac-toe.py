import cv2.cv2 as cv

game = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]


def print_board():
    i = 0
    while i < 3:
        print(f'{game[i][0]} | {game[i][1]} | {game[i][2]}')
        if i < 2:
            print('---------')
        i += 1


def user_turn():
    while True:
        try:
            x = input('Enter the position to enter: ')
            i = int(x[0])
            j = int(x[1])
            occupied = check(i, j)
            if occupied:
                print('Position occupied')
            else:
                break
        except IndexError:
            print('Enter a valid position')
    game[i][j] = 'X'


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


print_board()
while True:
    user_turn()
    if declareWinner(game) == 1:
        print_board()
        print('You have won the game')
        break
    computer_turn()
    if declareWinner(game) == -1:
        print_board()
        print('Computer has won the game')
        break
    print_board()
    if board_is_full():
        if declareWinner(game) == 0:
            print('Tie')
        break
