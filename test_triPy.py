# Triple TriPy Testing suite

import unittest
# from tripleTriPy import tripleTriPy

class TestBoard(unittest.TestCase):
	"""
	Test suite for board functions.
	"""

	def test_empty(self):
		"""
		Test board constructor to ensure an empty board is created properly.
		REMEMBER: Each list is an individual row!
		ex. board[0][2] is the 0th row, 3rd item across.
		"""
		self.assertEqual(Board(), [['x', 'x', 'x'], ['x','x', 'x'], ['x', 'x', 'x']])

class TestCards(unittest.TestCase):
	"""
	Test suite for card functions.
	"""

	def test_card(self):
		"""
		Tests that a card was created correctly
		REMEMBER: The first parameter in creating a card is rank sorted [up, down, left, right].
				  The second parameter is which player owns the card.
		ex. The sample_card below looks exactly like:
		   		-----------
		   		|	 2	  |
		   		| 4  A  8 |
		   		|    8    |
		   		-----------
		"""
		self.sample_card = Card([2, 8, 4, 8], A)
		self.assertEqual(self.sample_card.top(), 2)
		self.assertEqual(self.sample_card.bottom(), 8)
		self.assertEqual(self.sample_card.left(), 4)
		self.assertEqual(self.sample_card.right(), 8)
		self.assertEqual(self.sample_card.owner(), A)