# Triple TriPy Testing suite

import unittest
from Board import *
from Card import *

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
        self.board = Board()
        self.assertEqual(self.board.state[0], ['x', 'x', 'x'])
        self.assertEqual(self.board.state[1], ['x', 'x', 'x'])
        self.assertEqual(self.board.state[2], ['x', 'x', 'x'])


    def test_get_card_empty(self):
        """
		Test getting card in empty slot
		"""
        self.board = Board()
        self.assertEqual(self.board.get_card(1, 1), 'x')

    def test_place_get_card(self):
        """
		Test board state is correct after placing a card
		"""
        self.sample_card = Card([2, 8, 4, 8], 'A')
        self.board = Board()
        self.board.place(self.sample_card, 0, 0)

        self.assertEqual(self.board.get_card(0, 0), self.sample_card)


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
        self.sample_card = Card([2, 8, 4, 8], 'A')
        self.assertEqual(self.sample_card.top(), 2)
        self.assertEqual(self.sample_card.bottom(), 8)
        self.assertEqual(self.sample_card.left(), 4)
        self.assertEqual(self.sample_card.right(), 8)
        self.assertEqual(self.sample_card.owner(), 'A')

