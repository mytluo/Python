from Card.py import Card

class Hand:
    """
    One object of class Hand stores a number of Card objects.
    """
    def __init__(self, num_cards_in_hand):
        """
        :param num_cards_in_hand: integer (number of Card objects to generate)
        randomly generate Card objects given num_cards_in_hand and store in Hand object
        """
        self.hand_list = list()
        while num_cards_in_hand > 0:
            unique_card = True
            single_card = Card()
            for card in self.hand_list:
                if single_card == card:
                    unique_card = False
                    continue
            if unique_card:
                self.hand_list.append(single_card)
                num_cards_in_hand -= 1

    def bjValue(self):
        """
        Goes through each Card object stored in Hand object and gets its Blackjack value.
        Returns sum of all Blackjack values.
        """
        bj_sum = 0
        for card in self.hand_list:
            bj_sum += card.bjValue()
        return bj_sum

    def hitMe(self):
        """
        Generates a new unique card (not already in Hand) and adds it to the Hand object.
        """
        while True:
            add_card = Card()
            unique_card = True
            for card in self.hand_list:
                if add_card == card:
                    unique_card = False
                    continue
            if unique_card:
                self.hand_list.append(add_card)
                break

    def __str__(self):
        """
        Returns a comma-separated string of the Card objects in the Hand object.
        """
        return ", ".join(map(str, sorted(self.hand_list)))
