from random import choice
from functools import total_ordering

@total_ordering
class Card:
    """ One object of Card class creates a standard card with its rank and suit.
    """
    def __init__(self):
        """ Instantiates a Card object with randomly assigned rank and suit.
        """
        suits = ("s", "h", "c", "d")
        ranks = range(1, 14)
        self.rank = choice(ranks)
        self.suit = choice(suits)

    def getRank(self):
        """ Returns the rank of the object (from the rank_names dictionary) that calls the function.
        """
        rank_names = {
            1: "Ace",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Jack",
            12: "Queen",
            13: "King"
        }
        return rank_names[self.rank]

    def getSuit(self):
        """ Returns the suit of the object (from the suit_names dictionary) that calls the function.
        """
        suit_names = {
            "d": "Diamonds",
            "c": "Clubs",
            "h": "Hearts",
            "s": "Spades"
        }
        return suit_names[self.suit]


    def bjValue(self):
        """ Returns the blackjack value of the object that calls the function, with aces having the value of 1 and face
            cards (ranks 11, 12, and 13) having the value of 10.
        """
        if self.rank < 10:
            return self.rank
        else:
            return 10

    def __eq__(self, other):
        """ Returns True if the Card object have the same rank and suit.
            Returns False otherwise.
        """
        return (self.rank == other.rank) and (self.suit == other.suit)

    def __lt__(self, other):
        """ Returns True if the rank of self is less than rank of other.
            Returns False otherwise.
        """
        return (self.rank < other.rank)

    def __str__(self):
        """ Returns a string that names the card with its rank and suit.
        """
        return "%s of %s" %(Card.getRank(self), Card.getSuit(self))
