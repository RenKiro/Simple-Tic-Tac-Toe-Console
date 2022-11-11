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
