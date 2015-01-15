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