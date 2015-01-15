"""
Main class for board creation, and board state
"""

class Board(object):
	"""
	An empty board is a 2D array of 3x3 size where each row
	is represented by one of three internal lists. An 'x' 
	represents an unoccupied position.
	"""

	def __init__(self):
		state = [['x', 'x', 'x'], ['x', 'x', 'x'], ['x', 'x', 'x']]

	def __eq__(self, other):
		return self.state == other.state

	def get_card(self, row, col):
		"""
		Return the card stored in row row and col col of board
		"""
		return self.state[row][col]

	def place(self, card, row, col):
		"""
		Return none, and adds Card card to state of board
		"""
		self.state[row][col] = card
		return None 
