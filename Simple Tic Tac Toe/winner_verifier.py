# SAMPLE_PATTERN = None


def check_winning_pattern(letter, board):
	if letter == 'X':

		# check for horizontal winning pattern
		if board[(0, 0)] == 'X' and board[(0, 1)] == 'X' and board[(0, 2)] == 'X':
			return True
		elif board[(1, 0)] == 'X' and board[(1, 1)] == 'X' and board[(1, 2)] == 'X':
			return True
		elif board[(2, 0)] == 'X' and board[(2, 1)] == 'X' and board[(2, 2)] == 'X':
			return True

		# check for vertical winning pattern
		elif board[(0, 0)] == 'X' and board[(1, 0)] == 'X' and board[(2, 0)] == 'X':
			return True
		elif board[(0, 1)] == 'X' and board[(1, 1)] == 'X' and board[(2, 1)] == 'X':
			return True
		elif board[(0, 2)] == 'X' and board[(1, 2)] == 'X' and board[(2, 2)] == 'X':
			return True

		# check for diagonal winning pattern
		elif board[(0, 0)] == 'X' and board[(1, 1)] == 'X' and board[(2, 2)] == 'X':
			return True
		elif board[(0, 2)] == 'X' and board[(1, 1)] == 'X' and board[(2, 0)] == 'X':
			return True

		return False

	else:

		# check for horizontal winning pattern
		if board[(0, 0)] == 'O' and board[(0, 1)] == 'O' and board[(0, 2)] == 'O':
			return True
		elif board[(1, 0)] == 'O' and board[(1, 1)] == 'O' and board[(1, 2)] == 'O':
			return True
		elif board[(2, 0)] == 'O' and board[(2, 1)] == 'O' and board[(2, 2)] == 'O':
			return True

		# check for vertical winning pattern
		elif board[(0, 0)] == 'O' and board[(1, 0)] == 'O' and board[(2, 0)] == 'O':
			return True
		elif board[(0, 1)] == 'O' and board[(1, 1)] == 'O' and board[(2, 1)] == 'O':
			return True
		elif board[(0, 2)] == 'O' and board[(1, 2)] == 'O' and board[(2, 2)] == 'O':
			return True

		# check for diagonal winning pattern
		elif board[(0, 0)] == 'O' and board[(1, 1)] == 'O' and board[(2, 2)] == 'O':
			return True
		elif board[(0, 2)] == 'O' and board[(1, 1)] == 'O' and board[(2, 0)] == 'O':
			return True

		return False

	# if letter == 'X':
	# 	for row in SAMPLE_PATTERN:
	# 		if 'O' in row:
	# 			o_count = row.count('O')
	# 			for x in range(o_count):
	# 				idx = row.index('O')
	# 				row[idx] = ''
	# 	for pat in SAMPLE_PATTERN:
	# 		print(pat)

	# 	if SAMPLE_PATTERN in x_winning_patterns:
	# 		return True
	# else:
	# 	for row in SAMPLE_PATTERN:
	# 		if 'X' in row:
	# 			o_count = row.count('X')
	# 			for x in range(o_count):
	# 				idx = row.index('X')
	# 				row[idx] = ''

	# 	if SAMPLE_PATTERN in o_winning_patterns:
	# 		return True
	# return False


































# import os, time
# from winner_verifier import check_winning_pattern


# # global variables
# board = [
#     ['', '', ''],
#     ['', '', ''],
#     ['', '', '']
# ]


# # lambda f'ns
# clear = lambda: os.system('cls')
# wait = lambda sec: time.sleep(sec)


# # regular fn's
# def show_board(p1_score=0, p2_score=0):
#     real_board = f''' TIC TAC TOE \n
#     \t                  \t\t Player 1 SCORE: {p1_score}
#     \t       |     |    \t\t Player 2 SCORE: {p2_score}
#     \t    {board[0][0]} \t  {board[0][1]} \t{board[0][2]}
#     \t  _____|_____|_____
#     \t       |     |
#     \t    {board[1][0]} \t  {board[1][1]} \t{board[1][2]}
#     \t  _____|_____|_____
#     \t       |     | 
#     \t    {board[2][0]} \t  {board[2][1]} \t{board[2][2]}
#     \t       |     |
#     '''
#     clear()
#     print(real_board)

# def is_occupied(row, col):
#     if board[row][col]:
#         return True
#     return

# def is_fully_occupied():
#     full_count = 0
#     for row in board:
#         if '' not in row:
#             full_count += 1
#     if full_count == 3:
#         return True
#     return False

# def play():
#     player_one_score = 0
#     player_two_score = 0
#     game_over = False
#     is_win = False

#     while not game_over:
#         while True:
#             show_board()

#             if is_fully_occupied():
#                 print('\n Draw Match\n\n Game Over.')
#                 exit()

#             print('\n Player 1\'s Turn!\n\n (Enter your row-column coordinates)\n')
#             p1_row = int(input('\tEnter the row coordinate: '))
#             p1_col = int(input('\tEnter the column coordinate: '))

#             if is_occupied(p1_row, p1_col):
#                 input('\n Occupied already! Please try again.')
#                 continue

#             else:
#                 board[p1_row][p1_col] = 'X'
#                 is_win = check_winning_pattern('X', board)

#                 if is_win:
#                     show_board()
#                     print('\n Player 1 Won the match!')
#                     exit()
#                 break

#         while True:
#             show_board()

#             if is_fully_occupied():
#                 print('\n Draw Match\n\n Game Over.')
#                 exit()

#             print('\n Player 2\'s Turn!\n\n (Enter your row-column coordinates)\n')
#             p2_row = int(input('\tEnter the row coordinate: '))
#             p2_col = int(input('\tEnter the column coordinate: '))

#             if is_occupied(p2_row, p2_col):
#                 input('\n Occupied already! Please try again.')
#                 continue

#             else:
#                 board[p2_row][p2_col] = 'O'
#                 is_win = check_winning_pattern('O', board)

#                 if is_win:
#                     show_board()
#                     print('\n Player 2 Won the match!')
#                     exit()
#                 break

            

# if __name__ == '__main__':
#     play()
