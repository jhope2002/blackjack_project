from random import randint

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
names_and_values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

class Card:
    
    def __init__(self, name, suit):
        self.name = name
        self.suit = suit
        self.value = names_and_values[name]

    def __repr__(self):
        return f"{self.name}, {self.suit}, {self.value}"

    def __str__(self):
        return """
        ********
         {name}
         of   
         {suit}
        ********
        """.format(name = self.name, suit = self.suit)

class Deck:

    def __init__(self):
        self.cards = []
        self.build()    
    
    def __repr__(self):
        pass

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

class Dealer:

    def __init__(self):
        self.cards = []        

    def __repr__(self):
        pass

    def __str__(self):
        dealer_cards = "\nDEALER - " 
        for card in self.cards:
            dealer_cards += str(card)
        return dealer_cards    

    def add_card(self, card):
        self.cards.append(card)
    
    def card_total(self):
        total = 0
        for card in self.cards:
            total += card.value
        return total

class Player:

    def __init__(self, name):
        self.name = name
        self.cards = []
    
        def __repr__(self):
            pass

    def __str__(self):
        player_cards = f"\n{self.name} - " 
        for card in self.cards:
            player_cards += str(card)
        return player_cards    
        
    def add_card(self, card):
        self.cards.append(card)        

    def card_total(self):
        total = 0
        for card in self.cards:
            total += card.value
        return total

def deal(dealer, player):
    player.add_card(deck.draw_card())
    dealer.add_card(deck.draw_card())
    player.add_card(deck.draw_card())
    dealer.add_card(deck.draw_card())    

def hit(player):
    player.add_card(deck.draw_card())

deck = Deck()
deck.shuffle()

dealer = Dealer()
player1 = Player("Jeff")

deal(dealer, player1)

print(dealer)
print(f"Dealer has {dealer.card_total()} Points")
print(player1)
print(f"{player1.name} has {player1.card_total()} Points")

hit(player1)

print(player1.cards[-1])
print(f"{player1.name} has {player1.card_total()} Points")

def greet():
    print("Welcome to Blackjack")

def blackjack():
    greet()