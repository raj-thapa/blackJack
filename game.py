import random 

suits = ('Clubs', 'Diamonds', 'Spades' , 'Hearts')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}
playing = True


#creating a card class

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank + " of " + self.suit

#creating a deck class

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deckComp = ''
        for card in self.deck:
            deckComp += '\n' + card.__str__()
        return "The deck has: " + deckComp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


#creating a hand class
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    def add_cards(self,card):
        self.cards.append(card)
        self.value += values[card.rank]

        if card.rank == 'Ace':
            self.aces += 1

    def adjust_ace(self):
        while self.aces and self.value > 21:
            self.value -= 10
            self.aces -= 1

#creating a chips class
class Chips:
    def __init__(self, total = 100):
        self.total = total 
        self.bet = 0

    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet

#taking bets

def take_bet(chips):
    while True:
        try:
            chips.bet = int (input("How many chips would you like to bet? "))
        except:
            print("Sorry, a bet should be integer.")
        else:
            if chips.bet > chips.total:
                print("Sorry, not enough chips. You have: {}".format(chips.total))
            else:
                break

#taking hits

def hit(deck, hand):

    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_ace()

def hit_or_stand(deck, hand):
    global playing 

    while True:
        x = input("Enter h for hit or s for stand")
        if x[0].lower() == 'h':
            hit(deck,hand)
        elif x[0].lower() == 's':
            print("Dealer is playing. Player Stands.")
            playing = False
        else:
            print("Try Again!!!")
            continue
        break

def show_some(player, dealer):
    print("\n Dealer's Hand: ")
    print("First card hidden!")
    print(dealer.cards[1])

    print("\nPlayer's hand:")
    for card in player.cards:
        print(card)

def show_all(player, dealer):
    print("\n Dealer's hand:")
    for card in dealer.cards:
        print(card)
    print("Value of Dealer's hand is: {}".format(dealer.value))

    print("\n Player's hand:")
    for card in player.cards:
        print(card)
    print("Value of Dealr's hand is: {}".format(player.value))

def player_busts(player, dealer, chips):
    print("Bust Player!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player Wins!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Player wins! Dealer Busted!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()

def push(player, dealer):
    print("Dealer and player tie! Push")

while True:

    print("BLACK JACK !!!")
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_cards(deck.deal())
    player_hand.add_cards(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_cards(deck.deal())
    dealer_hand.add_cards(deck.deal())


    player_chips = Chips()

    take_bet(player_chips)

    show_some(player_hand, dealer_hand)

    while playing:
        hit_or_stand(deck,player_hand)

        show_some(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)

            break

    if player_hand.value<= 21:

        while dealer_hand.value < player_hand.value:
            hit(deck, dealer_hand)

        show_all(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)

    print('\n Player total chips are at: {}'.format(player_chips.total))

    new_game = input("Play another hand? y/n")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing!")
        break







        