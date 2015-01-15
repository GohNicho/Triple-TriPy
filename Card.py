"""
Main class for Card object and related functions
"""

class Card(object):
    """
    A card consists of two separate elements, a list rank that denotes rank
    and a identifier for which player it belongs to
    """

    def __init__(self, rank, player):
        self.rank = rank
        self.player = player

    def top(self):
        return self.rank[0]

    def bottom(self):
        return self.rank[1]

    def left(self):
        return self.rank[2]

    def right(self):
        return self.rank[3]

    def owner(self):
        return self.player