from random import randint

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
names_and_values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':10}

class Card:
    
    def __init__(self, name, suit):
        self.name = name
        self.suit = suit
        self.value = names_and_values[name]

    def __repr__(self):
        return f"{self.name}, {self.suit}, {self.value}"

    def __str__(self):
        return f"{self.name} of {self.suit}"

class Deck:

    def __init__(self):
        self.cards = []
        self.build()    
    
    def __repr__(self):
        return 

    def __str__(self):
        deck_string = ""
        for card in self.cards:
            deck_string += (str(card) + "\n")
        return deck_string        
    
    def build(self):
        suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
        names_and_values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':10}
        self.cards = [Card(name, suit) for suit in suits for name in names_and_values.keys()]

    def shuffle(self):
        for i in range(len(self.cards) - 1, 0, -1):
            r = randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def draw_card(self):
        return self.cards.pop(0)

blackjack_deck = Deck()

def greet():
    print("Welcome to Blackjack")