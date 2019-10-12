import random

class Card(object):
    suit_names_l2h = ["Clubs", "Diamonds", "Hearts", "Spades"]
    rank_names_l2h = ["Ace", "2", "3", "4", "5", "6", "7",
                  "8", "9", "10", "Jack", "Queen", "King"]

    def __repr__(self):
        return 'Card("{}", "{}")'.format(self.suit, self.rank)

    def __init__(self, suit, rank):
        rank = str(rank)
        if suit not in self.suit_names_l2h:
            raise ValueError("Suit {} is a valid suitname. Choose from {}".format(
                suit, str(self.suit_names_l2h)))
        if rank not in self.rank_names_l2h:
            raise ValueError("Rank {} is a valid Rankname. Choose from {}".format(
                rank, str(self.rank_names_l2h)))
        self.suit = suit.title()
        self.rank = rank.title()

    def __cmp__(self, other):
        return cmp((self.suit, self.rank), (other.suit, other.rank))


class Deck(object):

    @staticmethod
    def get_cards():
        cards = []
        for suit in Card.suit_names_l2h:
            for rank in Card.rank_names_l2h:
                cards.append(Card(suit, rank))
        return cards

    def __init__(self):
        self.cards = self.get_cards()

    def shuffle(self):
        random.shuffle(self.cards)

    def add_card(self, card):
        self.cards.append(card)



c1 = Card("Clubs", "7")
c2 = Card("Clubs", "3")
print(c1 > c2)