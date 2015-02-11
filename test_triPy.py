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

class TestWins(unittest.TestCase):
    """
    Specific test suite for checking win states
    """

    def setUp(self):
        """
        Initialize boards for testing purposes
        """
        self.board_A_win = Board()
        self.board_B_win = Board()
        self.board_draw = Board()

        self.card1 = Card([1, 1, 1, 1], 'A')
        self.card2 = Card([1, 1, 1, 1], 'A')
        self.card3 = Card([1, 1, 1, 1], 'A')
        self.card4 = Card([1, 1, 1, 1], 'A')
        self.card5 = Card([1, 1, 1, 1], 'A')
        self.card6 = Card([1, 1, 1, 1], 'A')
        self.card7 = Card([1, 1, 1, 1], 'B')
        self.card8 = Card([1, 1, 1, 1], 'B')
        self.card9 = Card([1, 1, 1, 1], 'B')
        self.card10 = Card([1, 1, 1, 1], 'B')
        self.card11 = Card([1, 1, 1, 1], 'B')

        self.board_A_win.place(self.card1, 0, 0)
        self.board_A_win.place(self.card2, 0, 1)
        self.board_A_win.place(self.card3, 0, 2)
        self.board_A_win.place(self.card4, 1, 0)
        self.board_A_win.place(self.card5, 1, 1)
        self.board_A_win.place(self.card6, 1, 2)
        self.board_A_win.place(self.card7, 2, 0)
        self.board_A_win.place(self.card8, 2, 1)
        self.board_A_win.place(self.card9, 2, 2)

        self.board_B_win.place(self.card10, 0, 0)
        self.board_B_win.place(self.card11, 0, 1)
        self.board_B_win.place(self.card3, 0, 2)
        self.board_B_win.place(self.card4, 1, 0)
        self.board_B_win.place(self.card5, 1, 1)
        self.board_B_win.place(self.card6, 1, 2)
        self.board_B_win.place(self.card7, 2, 0)
        self.board_B_win.place(self.card8, 2, 1)
        self.board_B_win.place(self.card9, 2, 2)

        self.board_draw.place(self.card10, 0, 0)
        self.board_draw.place(self.card2, 0, 1)
        self.board_draw.place(self.card3, 0, 2)
        self.board_draw.place(self.card4, 1, 0)
        self.board_draw.place(self.card5, 1, 1)
        self.board_draw.place(self.card6, 1, 2)
        self.board_draw.place(self.card7, 2, 0)
        self.board_draw.place(self.card8, 2, 1)
        self.board_draw.place(self.card9, 2, 2)

    def test_check_win_A(self):
        """
        Checks board in the case of a victory by player A
        """
        pass


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

