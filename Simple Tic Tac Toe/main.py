import os
import time
from winner_verifier import check_winning_pattern


# global variables
board = {
    (0, 0): 'A', (0, 1): 'B', (0, 2): 'C',
    (1, 0): 'D', (1, 1): 'E', (1, 2): 'F',
    (2, 0): 'G', (2, 1): 'H', (2, 2): 'I',
}


# lambda f'ns
clear = lambda: os.system('cls')
wait = lambda sec: time.sleep(sec)


# regular fn's
def show_board(p1_score=0, p2_score=0):
    real_board = f''' TIC TAC TOE \n
    \t                  \t\t Player 1 SCORE: {p1_score}
    \t       |     |    \t\t Player 2 SCORE: {p2_score}
    \t    {board[(0, 0)]} \t  {board[(0, 1)]} \t{board[(0, 2)]}
    \t  _____|_____|_____
    \t       |     |
    \t    {board[(1, 0)]} \t  {board[(1, 1)]} \t{board[(1, 2)]}
    \t  _____|_____|_____
    \t       |     | 
    \t    {board[(2, 0)]} \t  {board[(2, 1)]} \t{board[(2, 2)]}
    \t       |     |
    '''
    clear()
    print(real_board)

def is_occupied(board, letter):
    for row in board.keys():
        if board[row] == letter:
            return False, row
    return True, None

def is_fully_occupied():
    nl = board.values()
    if ('A' not in nl and 'B' not in nl and 
        'C' not in nl and 'D' not in nl and 
        'E' not in nl and 'F' not in nl and 
        'G' not in nl and 'H' not in nl and 
        'I' not in nl):
        return True
    return False

def play():
#     player_one_score = 0
#     player_two_score = 0
    game_over = False
    is_win = False

    while not game_over:
        while True:
            show_board()

            if is_fully_occupied():
                print('\n Draw Match\n\n Game Over.')
                exit()

            print('\n Player 1\'s Turn!\n\n (Draw your turn using a letter)\n')
            attack = input('\tWhich letter: ').upper()

            verify = is_occupied(board, attack)

            if verify[0]:
                input('\n Occupied already! Please try again.')
                continue

            if attack not in board.values():
                print('\n Unknown entry!')
                wait(2)
                continue

            else:
                board[verify[1]] = 'X'
                is_win = check_winning_pattern('X', board)

                if is_win:
                    show_board()
                    print('\n Player 1 Won the match!')
                    exit()
                break

        while True:
            show_board()

            if is_fully_occupied():
                print('\n Draw Match\n\n Game Over.')
                exit()

            print('\n Player 2\'s Turn!\n\n (Draw your turn using a letter)\n')
            attack = input('\tWhich letter: ').upper()

            verify = is_occupied(board, attack)

            if verify[0]:
                input('\n Occupied already! Please try again.')
                continue

            if attack not in board.values():
                print('\n Unknown entry!')
                wait(2)
                continue

            else:
                board[verify[1]] = 'O'
                is_win = check_winning_pattern('O', board)

                if is_win:
                    show_board()
                    print('\n Player 2 Won the match!')
                    exit()
                break

            

if __name__ == '__main__':
    play()
